#!/bin/bash
#
# Infra Pilot - Docker Build Script
#
# This script builds Docker images for all services.
# Can push to registry if credentials are configured.

set -e

echo "🐳 Infra Pilot Docker Build"
echo "============================"

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
REGISTRY="${REGISTRY:-}"
SERVICES=(
    "services/service-core"
    "services/orchestrator-agent"
    "services/discord-service"
    "services/management-panel"
)

PUSH_IMAGES=false
BUILD_FAILED=0

# Helper functions
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Parse arguments
for arg in "$@"; do
    case $arg in
        --push)
            PUSH_IMAGES=true
            ;;
        --registry)
            REGISTRY="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Usage: $0 [--push] [--registry REGISTRY_URL]"
            exit 1
            ;;
    esac
done

# Check Docker
if ! command -v docker &> /dev/null; then
    log_error "Docker is not installed"
    exit 1
fi

log_success "Docker found: $(docker --version)"

# Get version/tag
VERSION=$(git describe --tags --always 2>/dev/null || echo "latest")
log_info "Using version tag: $VERSION"

# Build images
echo ""
log_info "Building Docker images..."

for service in "${SERVICES[@]}"; do
    if [ ! -d "$service" ]; then
        log_warning "Service directory not found: $service"
        continue
    fi

    SERVICE_NAME=$(basename "$service")
    DOCKER_FILE="$service/Dockerfile"

    # Check if Dockerfile exists
    if [ ! -f "$DOCKER_FILE" ]; then
        log_warning "Dockerfile not found for $SERVICE_NAME, skipping"
        continue
    fi

    IMAGE_NAME="infra-pilot-$SERVICE_NAME"
    IMAGE_TAG="$VERSION"

    if [ -n "$REGISTRY" ]; then
        IMAGE_NAME="$REGISTRY/$IMAGE_NAME"
    fi

    echo ""
    log_info "Building $SERVICE_NAME..."
    
    if docker build \
        -f "$DOCKER_FILE" \
        -t "$IMAGE_NAME:$IMAGE_TAG" \
        -t "$IMAGE_NAME:latest" \
        "$service"; then
        log_success "$SERVICE_NAME built successfully"
        
        # Push if requested
        if [ "$PUSH_IMAGES" = true ]; then
            if [ -n "$REGISTRY" ]; then
                log_info "Pushing $IMAGE_NAME:$IMAGE_TAG to registry..."
                docker push "$IMAGE_NAME:$IMAGE_TAG" || {
                    log_error "Failed to push $SERVICE_NAME"
                    ((BUILD_FAILED++))
                }
                docker push "$IMAGE_NAME:latest" || true
            else
                log_warning "No registry specified, skipping push"
            fi
        fi
    else
        log_error "Failed to build $SERVICE_NAME"
        ((BUILD_FAILED++))
    fi
done

# Summary
echo ""
if [ $BUILD_FAILED -eq 0 ]; then
    log_success "All builds completed successfully!"
    
    if [ "$PUSH_IMAGES" = true ] && [ -n "$REGISTRY" ]; then
        log_success "All images pushed to registry"
    elif [ "$PUSH_IMAGES" = true ]; then
        log_warning "Registry not configured, images not pushed"
    else
        log_info "To push images, run: $0 --push --registry YOUR_REGISTRY"
    fi
    
    echo ""
    log_info "Built images:"
    docker images | grep infra-pilot || true
    
    exit 0
else
    log_error "$BUILD_FAILED build(s) failed"
    exit 1
fi
