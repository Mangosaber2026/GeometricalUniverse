import {
    mkdir,
    access,
    readdir
} from "node:fs/promises";

export async function createDirectory(
    path: string
): Promise<void> {

    await mkdir(path, {
        recursive: true
    });
}

export async function directoryExists(
    path: string
): Promise<boolean> {

    try {
        await access(path);
        return true;
    } catch {
        return false;
    }
}

export async function fileExists(
    path: string
): Promise<boolean> {
    try {
        await access(path);
        return true;
    } catch {
        return false;
    }
}