import time
import os

# Maze: 1 = jalan, 0 = tembok
maze = [
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1]
]

N = len(maze)
path = [[0]*N for _ in range(N)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze(x, y):
    clear_screen()
    print("=== RAT IN A MAZE (BACKTRACKING) ===\n")

    for i in range(N):
        for j in range(N):

            if i == x and j == y:
                print("🐭", end=" ")  # posisi tikus

            elif i == N-1 and j == N-1:
                print("🧀", end=" ")  # tujuan

            elif maze[i][j] == 0:
                print("⬛", end=" ")  # tembok

            elif path[i][j] == 1:
                print("🟩", end=" ")  # jalur

            else:
                print("⬜", end=" ")  # jalan kosong

        print()

    time.sleep(0.4)

# Fungsi backtracking
def solve(x, y):

    # Jika sampai tujuan
    if x == N-1 and y == N-1:
        path[x][y] = 1
        print_maze(x, y)
        print("\n🎉 SOLUSI DITEMUKAN! Tikus menemukan keju 🧀")
        return True

    # Cek valid
    if 0 <= x < N and 0 <= y < N and maze[x][y] == 1 and path[x][y] == 0:

        path[x][y] = 1
        print_maze(x, y)

        # Coba 4 arah
        if solve(x+1, y): return True  # bawah
        if solve(x, y+1): return True  # kanan
        if solve(x-1, y): return True  # atas
        if solve(x, y-1): return True  # kiri

        # Backtracking
        path[x][y] = 0
        print_maze(x, y)

    return False

if __name__ == "__main__":
    print("Mulai pencarian...\n")
    time.sleep(1)

    if not solve(0, 0):
        print("❌ Tidak ada jalur ditemukan")