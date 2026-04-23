import React from 'react';

type Props = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  label: string;
};

export const BrandButton: React.FC<Props> = ({ label, ...rest }) => {
  return (
    <button className="px-4 py-2 rounded-md bg-brand-primary text-white hover:bg-brand-primary-dark" {...rest}>
      {label}
    </button>
  );
};

export default BrandButton;
