
import { readFile } from "node:fs/promises";
import { join } from "node:path";

import type { ReleasePackage } from "./packages.ts";

export async function readPackageVersion(
    repositoryRoot: string,
    packageInfo: ReleasePackage,
): Promise<string> {
    const filePath = join(
        repositoryRoot,
        packageInfo.directory,
        "pyproject.toml",
    );

    const content = await readFile(filePath, "utf8");

    let insideProjectSection = false;

    for (const line of content.split(/\r?\n/)) {
        const section = line.trim().match(/^\[([^\]]+)\]$/);

        if (section) {
            insideProjectSection = section[1] === "project";
            continue;
        }

        if (!insideProjectSection) {
            continue;
        }

        const version = line.match(
            /^\s*version\s*=\s*["']([^"']+)["']\s*(?:#.*)?$/,
        );

        if (version) {
            return version[1];
        }
    }

    throw new Error(
        `Could not find a static version in [project] of ${filePath}.`,
    );
}
