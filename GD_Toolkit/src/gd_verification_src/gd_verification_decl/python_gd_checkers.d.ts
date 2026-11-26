import { execFile } from "node:child_process";
import type * as types from "../types.js";


/**
 * Promisied version of execFile.
 */
export declare const execFileAsync: typeof execFile.__promisify__;


/**
 * Checks available Python interpreters and returns the versions.
 * 
 * @returns List of strings containing solely the Python version of the available Python interpreters.
 */
export declare function getPythonVersions(): Promise<string[]>;


/**
 * Takes a given Python version and checks whether its version follows the MAJOR.MINOR.PATCH versioning convention.
 * 
 * @param versionText - Python version.
 * @returns true if provided Python version is compatible, false otherwise.
 */
export declare function isCompatiblePythonVersion(versionText: string): boolean;


/**
 * Takes a given Python version and verifies its compatibility 
 * with the GeometricalDomination project.
 * 
 * @param versionText - Python version.
 * @returns true if provided Python version is compatible, false otherwise.
 */
export declare function checkPython(): Promise<boolean>;


/**
 * Retrieves information from the GeometricalDomination project regarding the name of the project, 
 * its current installed version, summary, location, and the current version in the source pyproject.toml.
 * 
 * @returns A dictionary containing the retrieved information, null otherwise.
 */
export declare function getInfoGD(): Promise<types.GDInfo | null>;