// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { env } from "~/env";

export function resolveServiceURL(path: string) {
  let BASE_URL = env.NEXT_PUBLIC_API_URL ?? "/api/";
  if (!BASE_URL.endsWith("/")) {
    BASE_URL += "/";
  }

  const origin = window.location.origin;
  BASE_URL = origin + BASE_URL;

  return new URL(path, BASE_URL).toString();
}
