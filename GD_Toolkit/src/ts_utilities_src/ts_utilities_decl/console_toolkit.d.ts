/**
 * This class contains functions to display messages in the terminal.
 */
export namespace ConsoleToolkit {

    /**
     * Displays a success message in the terminal in green.
     * 
     * @param message - The message to be displayed.
     * @returns Nothing
     */
    export function success(message: string): void;


    /**
     * Displays a warning message in the terminal in yellow.
     * 
     * @param message - The message to be displayed.
     * @returns Nothing
     */
    export function warning(message: string): void;

    /**
     * Displays an error message in the terminal in red.
     * 
     * @param message - The message to be displayed.
     * @returns Nothing
     */
    export function error(message: string): void;

    /**
     * Displays an information message in the terminal in blue.
     * 
     * @param message - The message to be displayed.
     * @returns Nothing
     */
    export function information(message: string): void;
    
    /**
     * Displays an achieved message in the terminal in purple.
     * 
     * @param message - The message to be displayed.
     * @returns Nothing
     */
    export function achieved(message: string): void;
}