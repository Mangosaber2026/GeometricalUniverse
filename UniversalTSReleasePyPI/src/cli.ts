import { fileURLToPath } from "node:url";
import { validateVersion } from "./validation.ts";

import {
    isPackageId,
    RELEASE_PACKAGES,
} from "./packages.ts";

import { readPackageVersion } from "./version.ts";

const repositoryRoot = fileURLToPath(
    new URL("../../", import.meta.url),
);

async function main(): Promise<void> {
    const argument = process.argv[2];

    console.log("\nUniversalTSReleasePyPI");
    console.log("======================");

    if (!argument) {
        console.log("\nUsage: npm run release -- <package>");
        console.log("\nAvailable packages: gd, uf, tx");
        process.exitCode = 1;
        return;
    }

    if (!isPackageId(argument)) {
        console.error(`\nUnknown package: ${argument}`);
        console.error("Available packages: gd, uf, tx");
        process.exitCode = 1;
        return;
    }

    const packageInfo = RELEASE_PACKAGES[argument];

    const version = await readPackageVersion(
        repositoryRoot,
        packageInfo,
    );

    validateVersion(version);

    const tag = `${packageInfo.tagPrefix}${version}`;

    console.log(`\nPackage: ${packageInfo.displayName}`);
    console.log(`PyPI project: ${packageInfo.pypiProject}`);
    console.log(`Version: ${version}`);
    console.log(`Release tag: ${tag}`);

    console.log("\nNo Git operations performed.");
}

main().catch((error: unknown) => {
    const message = error instanceof Error
        ? error.message
        : String(error);

    console.error(`\nRelease manager error: ${message}`);
    process.exitCode = 1;
});
