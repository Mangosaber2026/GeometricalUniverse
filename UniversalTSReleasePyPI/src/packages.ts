
export const RELEASE_PACKAGES = {
    gd: {
        displayName: "GeometricalDomination",
        directory: "GeometricalDomination",
        pypiProject: "geometricaldomination",
        tagPrefix: "gd-v",
    },

    uf: {
        displayName: "UniversalFunctions",
        directory: "UniversalFunctions",
        pypiProject: "universalfunctions",
        tagPrefix: "uf-v",
    },

    tx: {
        displayName: "TurtleExtension",
        directory: "TurtleExtension",
        pypiProject: "turtleextension",
        tagPrefix: "tx-v",
    },
} as const;

export type PackageId = keyof typeof RELEASE_PACKAGES;

export type ReleasePackage =
    (typeof RELEASE_PACKAGES)[PackageId];

export function isPackageId(value: string): value is PackageId {
    return Object.hasOwn(RELEASE_PACKAGES, value);
}
