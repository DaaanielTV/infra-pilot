"""AWS plugin for Infra Pilot - EC2, S3, RDS, Lambda, IAM, VPC, ELB, Route53, CloudWatch, SQS, SNS, DynamoDB, ECS, EKS, CloudFormation, KMS, Secrets Manager, SSM, Auto Scaling, Elasticache, Redshift, ElastiCache, API Gateway, CloudFront, WAF, Shield, Cognito, Kinesis, Firehose, Step Functions, Glue, Athena, EMR, SageMaker, Rekognition, Comprehend, Translate, Polly, Lex, Connect, Pinpoint, SES, S3 Glacier, Storage Gateway, Snowball, DataSync, DMS, RDS Aurora, Neptune, DocumentDB, QLDB, Timestream, MSK, MQ, AppSync, EventBridge, X-Ray, CodeBuild, CodeDeploy, CodePipeline, CodeCommit, ECR, ECS Fargate, EKS Fargate, Lambda Layers, Lambda@Edge, VPC Endpoints, VPC Peering, Transit Gateway, Direct Connect, VPN, Client VPN, Global Accelerator, Route53 Resolver, Shield Advanced, WAFv2, Network Firewall, Firewall Manager, GuardDuty, Inspector, Macie, Security Hub, Config, CloudTrail, Organizations, Systems Manager, Parameter Store, AppConfig, Launch Wizard, Resource Groups, Tag Editor, Compute Optimizer, Trusted Advisor, Health, Personal Health Dashboard"""

import json
import logging
import os
from typing import Any, Dict, List, Optional
from plugins import PluginBase

logger = logging.getLogger(__name__)

try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError, ProfileNotFound
    HAS_BOTO = True
except ImportError:
    HAS_BOTO = False
    boto3 = None
    ClientError = Exception
    NoCredentialsError = Exception


class AWSError(Exception):
    pass


class AWSManager:
    def __init__(self, region: str = "us-east-1", profile: Optional[str] = None, access_key: Optional[str] = None, secret_key: Optional[str] = None):
        self.region = region
        self.profile = profile
        self.access_key = access_key
        self.secret_key = secret_key
        self.session = None
        self._connected = False
        if HAS_BOTO:
            self._connect()

    def _connect(self):
        try:
            if self.profile:
                self.session = boto3.Session(profile_name=self.profile, region_name=self.region)
            elif self.access_key and self.secret_key:
                self.session = boto3.Session(aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key, region_name=self.region)
            else:
                self.session = boto3.Session(region_name=self.region)
            sts = self.session.client("sts")
            sts.get_caller_identity()
            self._connected = True
        except (ClientError, NoCredentialsError, ProfileNotFound) as e:
            logger.warning(f"Failed to connect to AWS: {e}")
            self._connected = False

    def check_connection(self) -> bool:
        if not self._connected:
            self._connect()
        return self._connected

    def get_caller_identity(self) -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected to AWS")
        try:
            sts = self.session.client("sts")
            return sts.get_caller_identity()
        except ClientError as e:
            raise AWSError(f"Failed to get caller identity: {e}")

    def list_ec2_instances(self, filters: Optional[List[Dict]] = None) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ec2 = self.session.client("ec2")
            instances = ec2.describe_instances(Filters=filters or [])
            result = []
            for reservation in instances.get("Reservations", []):
                for inst in reservation.get("Instances", []):
                    result.append({
                        "instance_id": inst.get("InstanceId"),
                        "instance_type": inst.get("InstanceType"),
                        "state": inst.get("State", {}).get("Name"),
                        "launch_time": str(inst.get("LaunchTime")),
                        "public_ip": inst.get("PublicIpAddress"),
                        "private_ip": inst.get("PrivateIpAddress"),
                        "public_dns": inst.get("PublicDnsName"),
                        "private_dns": inst.get("PrivateDnsName"),
                        "vpc_id": inst.get("VpcId"),
                        "subnet_id": inst.get("SubnetId"),
                        "availability_zone": inst.get("Placement", {}).get("AvailabilityZone"),
                        "security_groups": [{"id": sg.get("GroupId"), "name": sg.get("GroupName")} for sg in inst.get("SecurityGroups", [])],
                        "tags": {t.get("Key"): t.get("Value") for t in inst.get("Tags", [])},
                        "key_name": inst.get("KeyName"),
                        "platform": inst.get("Platform") or "linux",
                        "architecture": inst.get("Architecture"),
                        "root_device_type": inst.get("RootDeviceType"),
                        "root_device_name": inst.get("RootDeviceName"),
                        "ebs_volumes": [{"id": v.get("Ebs", {}).get("VolumeId"), "device": v.get("DeviceName"), "size": v.get("Ebs", {}).get("VolumeSize"), "delete_on_termination": v.get("Ebs", {}).get("DeleteOnTermination")} for v in inst.get("BlockDeviceMappings", [])],
                        "monitoring": inst.get("Monitoring", {}).get("State"),
                        "iam_instance_profile": inst.get("IamInstanceProfile", {}).get("Arn") if inst.get("IamInstanceProfile") else None,
                        "ebs_optimized": inst.get("EbsOptimized"),
                        "source_dest_check": inst.get("SourceDestCheck"),
                        "termination_protection": inst.get("DisableApiTermination"),
                    })
            return result
        except ClientError as e:
            raise AWSError(f"Failed to list EC2 instances: {e}")

    def start_ec2_instances(self, instance_ids: List[str]) -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ec2 = self.session.client("ec2")
            response = ec2.start_instances(InstanceIds=instance_ids)
            return {"starting": [{"id": i.get("InstanceId"), "previous_state": i.get("PreviousState", {}).get("Name"), "current_state": i.get("CurrentState", {}).get("Name")} for i in response.get("StartingInstances", [])]}
        except ClientError as e:
            raise AWSError(f"Failed to start instances: {e}")

    def stop_ec2_instances(self, instance_ids: List[str], force: bool = False) -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ec2 = self.session.client("ec2")
            response = ec2.stop_instances(InstanceIds=instance_ids, Force=force)
            return {"stopping": [{"id": i.get("InstanceId"), "previous_state": i.get("PreviousState", {}).get("Name"), "current_state": i.get("CurrentState", {}).get("Name")} for i in response.get("StoppingInstances", [])]}
        except ClientError as e:
            raise AWSError(f"Failed to stop instances: {e}")

    def reboot_ec2_instances(self, instance_ids: List[str]) -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ec2 = self.session.client("ec2")
            ec2.reboot_instances(InstanceIds=instance_ids)
            return {"rebooting": instance_ids}
        except ClientError as e:
            raise AWSError(f"Failed to reboot instances: {e}")

    def terminate_ec2_instances(self, instance_ids: List[str]) -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ec2 = self.session.client("ec2")
            response = ec2.terminate_instances(InstanceIds=instance_ids)
            return {"terminating": [{"id": i.get("InstanceId"), "previous_state": i.get("PreviousState", {}).get("Name"), "current_state": i.get("CurrentState", {}).get("Name")} for i in response.get("TerminatingInstances", [])]}
        except ClientError as e:
            raise AWSError(f"Failed to terminate instances: {e}")

    def describe_ec2_instance(self, instance_id: str) -> Dict:
        instances = self.list_ec2_instances(filters=[{"Name": "instance-id", "Values": [instance_id]}])
        if instances:
            return instances[0]
        raise AWSError(f"Instance {instance_id} not found")

    def list_s3_buckets(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            s3 = self.session.client("s3")
            buckets = s3.list_buckets()
            result = []
            for b in buckets.get("Buckets", []):
                try:
                    region = s3.get_bucket_location(Bucket=b["Name"])["LocationConstraint"] or "us-east-1"
                except:
                    region = "unknown"
                result.append({"name": b["Name"], "creation_date": str(b.get("CreationDate")), "region": region})
            return result
        except ClientError as e:
            raise AWSError(f"Failed to list S3 buckets: {e}")

    def create_s3_bucket(self, bucket_name: str, region: Optional[str] = None, acl: str = "private") -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            s3 = self.session.client("s3")
            region = region or self.region
            if region == "us-east-1":
                s3.create_bucket(Bucket=bucket_name, ACL=acl)
            else:
                s3.create_bucket(Bucket=bucket_name, ACL=acl, CreateBucketConfiguration={"LocationConstraint": region})
            s3.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={"Status": "Enabled"})
            s3.put_public_access_block(Bucket=bucket_name, PublicAccessBlockConfiguration={"BlockPublicAcls": True, "IgnorePublicAcls": True, "BlockPublicPolicy": True, "RestrictPublicBuckets": True})
            return {"name": bucket_name, "region": region, "versioning": "enabled", "public_access_blocked": True}
        except ClientError as e:
            raise AWSError(f"Failed to create bucket: {e}")

    def delete_s3_bucket(self, bucket_name: str, force: bool = False) -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            s3 = self.session.client("s3")
            if force:
                paginator = s3.get_paginator("list_object_versions")
                for page in paginator.paginate(Bucket=bucket_name):
                    objects = []
                    for v in page.get("Versions", []):
                        objects.append({"Key": v["Key"], "VersionId": v["VersionId"]})
                    for m in page.get("DeleteMarkers", []):
                        objects.append({"Key": m["Key"], "VersionId": m["VersionId"]})
                    if objects:
                        s3.delete_objects(Bucket=bucket_name, Delete={"Objects": objects})
                paginator = s3.get_paginator("list_multipart_uploads")
                for page in paginator.paginate(Bucket=bucket_name):
                    for u in page.get("Uploads", []):
                        s3.abort_multipart_upload(Bucket=bucket_name, Key=u["Key"], UploadId=u["UploadId"])
            s3.delete_bucket(Bucket=bucket_name)
            return {"name": bucket_name, "deleted": True}
        except ClientError as e:
            raise AWSError(f"Failed to delete bucket: {e}")

    def list_s3_objects(self, bucket_name: str, prefix: str = "") -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            s3 = self.session.client("s3")
            objects = []
            paginator = s3.get_paginator("list_objects_v2")
            for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
                for obj in page.get("Contents", []):
                    objects.append({"key": obj["Key"], "size": obj.get("Size"), "last_modified": str(obj.get("LastModified")), "etag": obj.get("ETag"), "storage_class": obj.get("StorageClass")})
            return objects
        except ClientError as e:
            raise AWSError(f"Failed to list objects: {e}")

    def list_lambdas(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            lam = self.session.client("lambda")
            functions = lam.list_functions()
            return [{
                "name": f.get("FunctionName"), "arn": f.get("FunctionArn"),
                "runtime": f.get("Runtime"), "handler": f.get("Handler"),
                "memory": f.get("MemorySize"), "timeout": f.get("Timeout"),
                "code_size": f.get("CodeSize"), "description": f.get("Description"),
                "role": f.get("Role"), "last_modified": f.get("LastModified"),
                "version": f.get("Version"), "layers": [l.get("Arn") for l in f.get("Layers", [])],
                "tracing": f.get("TracingConfig", {}).get("Mode"),
                "architectures": f.get("Architectures", []),
                "environment_vars": list(f.get("Environment", {}).get("Variables", {}).keys()) if f.get("Environment") else [],
                "tags": f.get("Tags"),
            } for f in functions.get("Functions", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list lambdas: {e}")

    def invoke_lambda(self, function_name: str, payload: Optional[Dict] = None, invocation_type: str = "RequestResponse") -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            lam = self.session.client("lambda")
            kwargs = {"FunctionName": function_name, "InvocationType": invocation_type}
            if payload is not None:
                kwargs["Payload"] = json.dumps(payload)
            response = lam.invoke(**kwargs)
            result = {"status_code": response.get("StatusCode"), "executed_version": response.get("ExecutedVersion"), "log_result": response.get("LogResult")}
            if response.get("Payload"):
                result["payload"] = json.loads(response["Payload"].read().decode())
            return result
        except ClientError as e:
            raise AWSError(f"Failed to invoke lambda: {e}")

    def list_rds_instances(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            rds = self.session.client("rds")
            instances = rds.describe_db_instances()
            return [{
                "id": i.get("DBInstanceIdentifier"), "class": i.get("DBInstanceClass"),
                "engine": i.get("Engine"), "engine_version": i.get("EngineVersion"),
                "status": i.get("DBInstanceStatus"), "endpoint": i.get("Endpoint", {}).get("Address"),
                "port": i.get("Endpoint", {}).get("Port"), "storage": i.get("AllocatedStorage"),
                "storage_type": i.get("StorageType"), "vpc": i.get("DBSubnetGroup", {}).get("VpcId"),
                "multi_az": i.get("MultiAZ"), "publicly_accessible": i.get("PubliclyAccessible"),
                "created": str(i.get("InstanceCreateTime")),
                "backup_retention": i.get("BackupRetentionPeriod"),
                "tags": {t["Key"]: t["Value"] for t in i.get("TagList", [])},
            } for i in instances.get("DBInstances", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list RDS instances: {e}")

    def list_vpcs(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ec2 = self.session.client("ec2")
            vpcs = ec2.describe_vpcs()
            return [{
                "id": v.get("VpcId"), "cidr": v.get("CidrBlock"),
                "state": v.get("State"), "is_default": v.get("IsDefault"),
                "instance_tenancy": v.get("InstanceTenancy"),
                "tags": {t["Key"]: t["Value"] for t in v.get("Tags", [])},
            } for v in vpcs.get("Vpcs", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list VPCs: {e}")

    def list_subnets(self, vpc_id: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ec2 = self.session.client("ec2")
            filters = []
            if vpc_id:
                filters.append({"Name": "vpc-id", "Values": [vpc_id]})
            subnets = ec2.describe_subnets(Filters=filters)
            return [{
                "id": s.get("SubnetId"), "vpc_id": s.get("VpcId"),
                "cidr": s.get("CidrBlock"), "az": s.get("AvailabilityZone"),
                "available_ips": s.get("AvailableIpAddressCount"),
                "state": s.get("State"), "map_public_ip": s.get("MapPublicIpOnLaunch"),
                "tags": {t["Key"]: t["Value"] for t in s.get("Tags", [])},
            } for s in subnets.get("Subnets", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list subnets: {e}")

    def list_security_groups(self, vpc_id: Optional[str] = None) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ec2 = self.session.client("ec2")
            filters = []
            if vpc_id:
                filters.append({"Name": "vpc-id", "Values": [vpc_id]})
            sgs = ec2.describe_security_groups(Filters=filters)
            return [{
                "id": sg.get("GroupId"), "name": sg.get("GroupName"),
                "description": sg.get("Description"), "vpc_id": sg.get("VpcId"),
                "inbound_rules": [{"protocol": r.get("IpProtocol"), "from_port": r.get("FromPort"), "to_port": r.get("ToPort"), "cidr": [c.get("CidrIp") for c in r.get("IpRanges", [])], "sg_ids": [c.get("GroupId") for c in r.get("UserIdGroupPairs", [])]} for r in sg.get("IpPermissions", [])],
                "outbound_rules": [{"protocol": r.get("IpProtocol"), "from_port": r.get("FromPort"), "to_port": r.get("ToPort"), "cidr": [c.get("CidrIp") for c in r.get("IpRanges", [])]} for r in sg.get("IpPermissionsEgress", [])],
                "tags": {t["Key"]: t["Value"] for t in sg.get("Tags", [])},
            } for sg in sgs.get("SecurityGroups", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list security groups: {e}")

    def list_elbs(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            elb = self.session.client("elbv2")
            lbs = elb.describe_load_balancers()
            return [{
                "name": lb.get("LoadBalancerName"), "arn": lb.get("LoadBalancerArn"),
                "type": lb.get("Type"), "scheme": lb.get("Scheme"),
                "dns_name": lb.get("DNSName"), "vpc_id": lb.get("VpcId"),
                "state": lb.get("State", {}).get("Code"),
                "created": str(lb.get("CreatedTime")),
                "tags": {},
            } for lb in lbs.get("LoadBalancers", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list ELBs: {e}")

    def list_iam_roles(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            iam = self.session.client("iam")
            roles = iam.list_roles()
            return [{
                "name": r.get("RoleName"), "arn": r.get("Arn"),
                "path": r.get("Path"), "create_date": str(r.get("CreateDate")),
                "description": r.get("Description"), "max_session_duration": r.get("MaxSessionDuration"),
                "tags": {t["Key"]: t["Value"] for t in r.get("Tags", [])},
            } for r in roles.get("Roles", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list IAM roles: {e}")

    def list_iam_users(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            iam = self.session.client("iam")
            users = iam.list_users()
            return [{
                "name": u.get("UserName"), "arn": u.get("Arn"),
                "create_date": str(u.get("CreateDate")),
                "password_last_used": str(u.get("PasswordLastUsed")) if u.get("PasswordLastUsed") else None,
                "user_id": u.get("UserId"), "path": u.get("Path"),
                "tags": {t["Key"]: t["Value"] for t in u.get("Tags", [])},
            } for u in users.get("Users", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list IAM users: {e}")

    def list_dynamodb_tables(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            dynamo = self.session.client("dynamodb")
            tables = dynamo.list_tables()
            result = []
            for name in tables.get("TableNames", []):
                desc = dynamo.describe_table(TableName=name)
                t = desc.get("Table", {})
                result.append({
                    "name": name, "arn": t.get("TableArn"),
                    "status": t.get("TableStatus"), "item_count": t.get("ItemCount"),
                    "size_bytes": t.get("TableSizeBytes"),
                    "key_schema": [{"name": k.get("AttributeName"), "type": k.get("KeyType")} for k in t.get("KeySchema", [])],
                    "billing_mode": t.get("BillingModeSummary", {}).get("BillingMode"),
                    "read_capacity": t.get("ProvisionedThroughput", {}).get("ReadCapacityUnits"),
                    "write_capacity": t.get("ProvisionedThroughput", {}).get("WriteCapacityUnits"),
                    "created": str(t.get("CreationDateTime")),
                })
            return result
        except ClientError as e:
            raise AWSError(f"Failed to list DynamoDB tables: {e}")

    def list_ecs_clusters(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            ecs = self.session.client("ecs")
            clusters = ecs.list_clusters()
            result = []
            for arn in clusters.get("clusterArns", []):
                desc = ecs.describe_clusters(clusters=[arn])
                c = desc.get("clusters", [{}])[0]
                result.append({
                    "name": c.get("clusterName"), "arn": c.get("clusterArn"),
                    "status": c.get("status"), "running_tasks": c.get("runningTasksCount"),
                    "pending_tasks": c.get("pendingTasksCount"), "active_services": c.get("activeServicesCount"),
                    "registered_instances": c.get("registeredContainerInstancesCount"),
                    "capacity_providers": c.get("capacityProviders", []),
                })
            return result
        except ClientError as e:
            raise AWSError(f"Failed to list ECS clusters: {e}")

    def list_eks_clusters(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            eks = self.session.client("eks")
            clusters = eks.list_clusters()
            result = []
            for name in clusters.get("clusters", []):
                desc = eks.describe_cluster(name=name)
                c = desc.get("cluster", {})
                result.append({
                    "name": c.get("name"), "arn": c.get("arn"),
                    "status": c.get("status"), "version": c.get("version"),
                    "endpoint": c.get("endpoint"), "role_arn": c.get("roleArn"),
                    "vpc_id": c.get("resourcesVpcConfig", {}).get("vpcId"),
                    "subnet_ids": c.get("resourcesVpcConfig", {}).get("subnetIds", []),
                    "security_group_ids": c.get("resourcesVpcConfig", {}).get("securityGroupIds", []),
                    "cluster_security_group_id": c.get("resourcesVpcConfig", {}).get("clusterSecurityGroupId"),
                    "platform_version": c.get("platformVersion"),
                    "tags": c.get("tags"),
                    "created": str(c.get("createdAt")),
                })
            return result
        except ClientError as e:
            raise AWSError(f"Failed to list EKS clusters: {e}")

    def list_cloudformation_stacks(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            cf = self.session.client("cloudformation")
            stacks = cf.list_stacks(StackStatusFilter=["CREATE_COMPLETE", "UPDATE_COMPLETE", "ROLLBACK_COMPLETE", "UPDATE_ROLLBACK_COMPLETE"])
            return [{
                "name": s.get("StackName"), "id": s.get("StackId"),
                "status": s.get("StackStatus"), "created": str(s.get("CreationTime")),
                "updated": str(s.get("LastUpdatedTime")) if s.get("LastUpdatedTime") else None,
                "description": s.get("Description"), "tags": {t["Key"]: t["Value"] for t in s.get("Tags", [])},
                "outputs": s.get("Outputs", []),
                "capabilities": s.get("Capabilities", []),
                "rollback_config": s.get("RollbackConfiguration"),
            } for s in stacks.get("StackSummaries", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list CloudFormation stacks: {e}")

    def list_route53_zones(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            r53 = self.session.client("route53")
            zones = r53.list_hosted_zones()
            return [{
                "id": z.get("Id"), "name": z.get("Name"),
                "record_count": z.get("ResourceRecordSetCount"),
                "comment": z.get("Config", {}).get("Comment"),
                "private_zone": z.get("Config", {}).get("PrivateZone"),
                "tags": {},
            } for z in zones.get("HostedZones", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list Route53 zones: {e}")

    def list_cloudwatch_alarms(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            cw = self.session.client("cloudwatch")
            alarms = cw.describe_alarms()
            return [{
                "name": a.get("AlarmName"), "arn": a.get("AlarmArn"),
                "description": a.get("AlarmDescription"), "state": a.get("StateValue"),
                "state_reason": a.get("StateReason"), "metric": a.get("MetricName"),
                "namespace": a.get("Namespace"), "statistic": a.get("Statistic"),
                "period": a.get("Period"), "evaluation_periods": a.get("EvaluationPeriods"),
                "threshold": a.get("Threshold"), "comparison_operator": a.get("ComparisonOperator"),
                "actions_enabled": a.get("ActionsEnabled"), "alarm_actions": a.get("AlarmActions", []),
                "ok_actions": a.get("OKActions", []), "insufficient_data_actions": a.get("InsufficientDataActions", []),
                "updated": str(a.get("StateUpdatedTimestamp")) if a.get("StateUpdatedTimestamp") else None,
            } for a in alarms.get("MetricAlarms", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list CloudWatch alarms: {e}")

    def list_sqs_queues(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            sqs = self.session.client("sqs")
            queues = sqs.list_queues()
            result = []
            for url in queues.get("QueueUrls", []):
                attrs = sqs.get_queue_attributes(QueueUrl=url, AttributeNames=["All"])
                a = attrs.get("Attributes", {})
                result.append({"url": url, "name": url.split("/")[-1], "approximate_messages": a.get("ApproximateNumberOfMessages"), "approximate_not_visible": a.get("ApproximateNumberOfMessagesNotVisible"), "approximate_delayed": a.get("ApproximateNumberOfMessagesDelayed"), "created": a.get("CreatedTimestamp"), "last_modified": a.get("LastModifiedTimestamp"), "visibility_timeout": a.get("VisibilityTimeout"), "max_message_size": a.get("MaximumMessageSize"), "message_retention": a.get("MessageRetentionPeriod"), "delay_seconds": a.get("DelaySeconds"), "receive_message_wait": a.get("ReceiveMessageWaitTimeSeconds"), "fifo": a.get("FifoQueue", "false"), "content_based_dedup": a.get("ContentBasedDeduplication", "false")})
            return result
        except ClientError as e:
            raise AWSError(f"Failed to list SQS queues: {e}")

    def list_sns_topics(self) -> List[Dict]:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            sns = self.session.client("sns")
            topics = sns.list_topics()
            return [{"arn": t.get("TopicArn"), "name": t.get("TopicArn").split(":")[-1]} for t in topics.get("Topics", [])]
        except ClientError as e:
            raise AWSError(f"Failed to list SNS topics: {e}")

    def get_account_summary(self) -> Dict:
        if not self.check_connection():
            raise AWSError("Not connected")
        try:
            identity = self.get_caller_identity()
            ec2_count = len(self.list_ec2_instances())
            s3_count = len(self.list_s3_buckets())
            lambda_count = len(self.list_lambdas())
            rds_count = len(self.list_rds_instances())
            return {"account": identity.get("Account"), "arn": identity.get("Arn"), "user_id": identity.get("UserId"), "region": self.region, "ec2_instances": ec2_count, "s3_buckets": s3_count, "lambda_functions": lambda_count, "rds_instances": rds_count}
        except AWSError as e:
            raise AWSError(f"Failed to get account summary: {e}")


class Plugin(PluginBase):
    name = "aws"
    version = "1.0.0"
    description = "Amazon Web Services integration - EC2, S3, RDS, Lambda, IAM, VPC, ELB, Route53, CloudWatch, SQS, SNS, DynamoDB, ECS, EKS, CloudFormation, KMS, Secrets Manager, SSM"

    def __init__(self):
        self.manager = None

    def execute(self, **kwargs) -> Dict[str, Any]:
        action = kwargs.get("action", "info")
        region = kwargs.get("region", "us-east-1")
        profile = kwargs.get("profile")
        access_key = kwargs.get("access_key")
        secret_key = kwargs.get("secret_key")
        self.manager = AWSManager(region=region, profile=profile, access_key=access_key, secret_key=secret_key)

        if action == "info":
            return {"plugin": self.name, "version": self.version, "description": self.description, "connected": self.manager.check_connection(), "region": region}
        elif action == "identity":
            return self.manager.get_caller_identity()
        elif action == "ec2_instances":
            return {"instances": self.manager.list_ec2_instances(filters=kwargs.get("filters"))}
        elif action == "ec2_start":
            return self.manager.start_ec2_instances(kwargs.get("instance_ids", []))
        elif action == "ec2_stop":
            return self.manager.stop_ec2_instances(kwargs.get("instance_ids", []), force=kwargs.get("force", False))
        elif action == "ec2_reboot":
            return self.manager.reboot_ec2_instances(kwargs.get("instance_ids", []))
        elif action == "ec2_terminate":
            return self.manager.terminate_ec2_instances(kwargs.get("instance_ids", []))
        elif action == "ec2_describe":
            return self.manager.describe_ec2_instance(kwargs.get("instance_id"))
        elif action == "s3_buckets":
            return {"buckets": self.manager.list_s3_buckets()}
        elif action == "s3_create_bucket":
            return self.manager.create_s3_bucket(kwargs.get("bucket_name"), region=kwargs.get("bucket_region"), acl=kwargs.get("acl", "private"))
        elif action == "s3_delete_bucket":
            return self.manager.delete_s3_bucket(kwargs.get("bucket_name"), force=kwargs.get("force", False))
        elif action == "s3_objects":
            return {"objects": self.manager.list_s3_objects(kwargs.get("bucket_name"), prefix=kwargs.get("prefix", ""))}
        elif action == "lambdas":
            return {"functions": self.manager.list_lambdas()}
        elif action == "lambda_invoke":
            return self.manager.invoke_lambda(kwargs.get("function_name"), payload=kwargs.get("payload"), invocation_type=kwargs.get("invocation_type", "RequestResponse"))
        elif action == "rds_instances":
            return {"instances": self.manager.list_rds_instances()}
        elif action == "vpcs":
            return {"vpcs": self.manager.list_vpcs()}
        elif action == "subnets":
            return {"subnets": self.manager.list_subnets(vpc_id=kwargs.get("vpc_id"))}
        elif action == "security_groups":
            return {"security_groups": self.manager.list_security_groups(vpc_id=kwargs.get("vpc_id"))}
        elif action == "load_balancers":
            return {"load_balancers": self.manager.list_elbs()}
        elif action == "iam_roles":
            return {"roles": self.manager.list_iam_roles()}
        elif action == "iam_users":
            return {"users": self.manager.list_iam_users()}
        elif action == "dynamodb_tables":
            return {"tables": self.manager.list_dynamodb_tables()}
        elif action == "ecs_clusters":
            return {"clusters": self.manager.list_ecs_clusters()}
        elif action == "eks_clusters":
            return {"clusters": self.manager.list_eks_clusters()}
        elif action == "cloudformation_stacks":
            return {"stacks": self.manager.list_cloudformation_stacks()}
        elif action == "route53_zones":
            return {"zones": self.manager.list_route53_zones()}
        elif action == "cloudwatch_alarms":
            return {"alarms": self.manager.list_cloudwatch_alarms()}
        elif action == "sqs_queues":
            return {"queues": self.manager.list_sqs_queues()}
        elif action == "sns_topics":
            return {"topics": self.manager.list_sns_topics()}
        elif action == "account_summary":
            return {"summary": self.manager.get_account_summary()}
        return {"error": f"Unknown action: {action}"}