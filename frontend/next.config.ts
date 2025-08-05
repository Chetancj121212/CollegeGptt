import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  experimental: {
    esmExternals: true,
  },
  transpilePackages: ['lucide-react'],
};

export default nextConfig;
