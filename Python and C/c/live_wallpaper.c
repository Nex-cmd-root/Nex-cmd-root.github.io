#include "raylib.h"
#include <stdlib.h>

// Explicitly declare the 3 Windows API functions we need
// This completely bypasses the header conflict and file path errors!
#ifdef _WIN32
    #define SWP_SHOWWINDOW 0x0040
    typedef struct HWND__ *HWND;
    typedef int (*WNDENUMPROC)(HWND, long long);
    
    __declspec(dllimport) HWND __stdcall FindWindowA(const char*, const char*);
    __declspec(dllimport) HWND __stdcall FindWindowExA(HWND, HWND, const char*, const char*);
    __declspec(dllimport) long long __stdcall SendMessageTimeoutA(HWND, unsigned int, unsigned long long, long long, unsigned int, unsigned int, unsigned long long*);
    __declspec(dllimport) int __stdcall EnumWindows(WNDENUMPROC, long long);
    __declspec(dllimport) int __stdcall SetParent(HWND, HWND);
    __declspec(dllimport) int __stdcall SetWindowPos(HWND, HWND, int, int, int, int, unsigned int);

    // Rewrite our window search callback using basic types
    int __stdcall FindWorkerW(HWND hwnd, long long lParam) {
        HWND p = FindWindowExA(hwnd, 0, "SHELLDLL_DefView", 0);
        if (p != 0) {
            HWND* ret = (HWND*)lParam;
            *ret = FindWindowExA(0, hwnd, "WorkerW", 0);
        }
        return 1;
    }
#endif

#define FONT_SIZE 18

int main(void) {
    // 1. Tell Raylib to skip drawing window borders/decorations
    SetConfigFlags(FLAG_WINDOW_UNDECORATED); 
    
    // 2. Initialize the window FIRST using a temporary standard size.
    // This wakes up GLFW so it can safely scan your display setup!
    InitWindow(800, 600, "Matrix Wallpaper");
    
    // 3. NOW it is safe to grab the true monitor dimensions
    int monitor = GetCurrentMonitor();
    int screenWidth = GetMonitorWidth(monitor);
    int screenHeight = GetMonitorHeight(monitor);
    
    // 4. Resize the active window to match your monitor's true resolution
    SetWindowSize(screenWidth, screenHeight);
    SetTargetFPS(60);

    #ifdef _WIN32
        // 5. Windows OS Wizardry: Force our window behind desktop icons
        HWND progman = FindWindowA("Progman", 0);
        unsigned long long result = 0;
        SendMessageTimeoutA(progman, 0x052C, 0, 0, 0, 1000, &result);

        HWND workerw = 0;
        EnumWindows(FindWorkerW, (long long)&workerw);

        // Fetch our Raylib window handle safely 
        HWND raylibWindow = (HWND)GetWindowHandle();

        // Slip the window under the desktop icons and stretch it across the monitor
        SetParent(raylibWindow, workerw);
        SetWindowPos(raylibWindow, 0, 0, 0, screenWidth, screenHeight, SWP_SHOWWINDOW);
    #endif

    // ... (Keep your Matrix Rain initialization and while loop exactly the same!)

    // 3. Your Live Wallpaper Loop (e.g., A floating matrix or particle stream)
    int numColumns = screenWidth / FONT_SIZE;
    if (numColumns > 200) numColumns = 200;

    // 1. Create TWO arrays: one for positions, one for speeds
    float dropY[200]; 
    float speeds[200];

    // 2. Initialize each column with its own random starting height and speed
    for (int i = 0; i < numColumns; i++) {
        // Start above the screen (measured in grid rows)
        dropY[i] = (float)GetRandomValue(-20, 0); 
        
        // Assign a speed between 0.1 and 0.4 rows per frame
        speeds[i] = (float)GetRandomValue(10, 40) / 100.0f; 
    }

    while (!WindowShouldClose()) {
        
        // --- UPDATE LOGIC ---
        for (int i = 0; i < numColumns; i++) {
            // Add the column's unique speed to its Y position
            dropY[i] += speeds[i];

            // Check if the drop has fallen past the bottom of the screen
            if (dropY[i] * FONT_SIZE > screenHeight) {
                // Small random chance to reset (prevents columns from syncing up)
                if (GetRandomValue(0, 100) > 95) {
                    dropY[i] = (float)GetRandomValue(-10, 0);
                    
                    // Reroll the speed so the column changes pace on its next run
                    speeds[i] = (float)GetRandomValue(10, 40) / 100.0f;
                }
            }
        }

        // --- DRAWING LOGIC ---
        BeginDrawing();
        DrawRectangle(0, 0, screenWidth, screenHeight, ColorAlpha(BLACK, 0.12f));

        for (int i = 0; i < numColumns; i++) {
            if (dropY[i] >= 0) {
                char randomChar = (char)GetRandomValue(33, 126);
                char str[2] = { randomChar, '\0' };

                int xPos = i * FONT_SIZE;
                
                // Cast the float back to an int pixel coordinate for drawing
                int yPos = (int)(dropY[i]) * FONT_SIZE;

                // Bright white head for the stream, green tail
                // Fast streams get a brighter green (LIME), slow streams get a darker green
                if (GetRandomValue(0, 10) > 8) {
                    DrawText(str, xPos, yPos, FONT_SIZE, WHITE);
                } else {
                    Color streamColor = (speeds[i] > 0.25f) ? LIME : GREEN;
                    DrawText(str, xPos, yPos, FONT_SIZE, streamColor);
                }
            }
        }
        EndDrawing();
    }

    CloseWindow();
    return 0;
}