
export function validateVersion(version: string): void {
    const pattern = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/;

    if (!pattern.test(version)) {
        throw new Error(
            `Invalid release version: "${version}". ` +
            "Expected MAJOR.MINOR.PATCH.",
        );
    }

    const parts = version.split(".");

    for (const part of parts) {
        if (!Number.isSafeInteger(Number(part))) {
            throw new Error(
                `Version component exceeds the safe integer range: ${part}`,
            );
        }
    }
}
