/**
 * Takes the relaive or absolute path of a certain file and returns its contents.
 * 
 * @param path - The absolute or relative path of desired file.
 * @returns - Contents of the file as a promise.
 */
export declare function readFile(path: string): Promise<string>;


/**
 * Takes the relative or absolute path of a certain file and replaces the current content with 
 * provided content.
 * 
 * @param path - The absolute or relative path of the desired file.
 * @param file_content - The content to replace the current content in the desired file.
 * @returns A promise that resolves without a value once the function has been executed.
 */
export declare function writeFile(path: string, file_content: string): Promise<void>;


/**
 * Takes the relative or absolute path of a certain file and adds the provided content as "content_to_add" 
 * to the desired file.
 * 
 * @param path - The absolute or relative path of the desired file.
 * @param content_to_add - The content to be added to the desired file.
 * @returns A promise that resolves without a value once the function has been executed.
 */
export declare function addToFile(path: string, content_to_add: string): Promise<void>;