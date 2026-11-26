import * as fs from "node:fs/promises";


export async function readFile(
    path: string
): Promise<string> {
    return await fs.readFile(path, "utf-8")
};

export async function writeFile(
    path: string,
    file_content: string
): Promise<void> {
    await fs.writeFile(path, file_content, "utf-8")
};

export async function addToFile(
    path: string,
    content_to_add: string
): Promise<void> {
    await fs.appendFile(path, content_to_add, "utf-8")
}