#!/usr/bin/env python3
"""
OS 程式填空互動測驗
涵蓋：Q24 (Σn! Shared Memory) / Q25 (2x+3y-5 Shared Memory) / Q26 (Shell Interface)
"""

import sys

# ANSI 色碼
G = '\033[92m'   # 綠色（正確）
R = '\033[91m'   # 紅色（錯誤）
Y = '\033[93m'   # 黃色（提示/答案）
C = '\033[96m'   # 青色（標題）
B = '\033[1m'    # 粗體
D = '\033[2m'    # 暗色
X = '\033[0m'    # 重置

def clr(text, code):
    return f"{code}{text}{X}"

def sep(char='─', n=62):
    print(clr(char * n, C))

score = 0
total = 0
wrong_list = []  # 記錄答錯的空格

# ─────────────────────────────────────────────────────────────
# 評分核心
# ─────────────────────────────────────────────────────────────

def normalize(s):
    """正規化字串：去頭尾空白、分號、合併空格"""
    return s.strip().rstrip(';').strip().replace('  ', ' ')

def grade(user_ans, accepted):
    """
    彈性比對：
    - 大小寫不敏感（函數名稱）
    - 忽略尾端分號
    - 忽略多餘空格
    """
    u = normalize(user_ans).lower().replace(' ', '')
    for a in accepted:
        a_norm = normalize(a).lower().replace(' ', '')
        if u == a_norm:
            return True
    return False


def ask(blank_id, context_line, description, accepted,
        hint=None, freeform=False, q_tag=""):
    """
    顯示一個空格題，讀取使用者答案，批改並回傳是否正確。

    freeform=True：顯示參考答案後讓使用者自評（適用多行程式碼）
    """
    global score, total, wrong_list
    total += 1

    print()
    sep('·')
    print(f"{B}空格 ({blank_id}){X}  {description}")
    print(clr(f"\n    {context_line}\n", D))
    if hint:
        print(clr(f"  💡 提示：{hint}", C))

    user = input("  填入 > ").strip()

    if freeform:
        # 自評模式：顯示答案，讓使用者判斷
        print(clr("\n  ✎ 參考答案：", Y))
        for a in accepted:
            for line in a.split('\n'):
                print(clr(f"      {line}", Y))
        yn = input("\n  你的答案正確嗎？(y/n) > ").strip().lower()
        correct = yn.startswith('y')
    else:
        correct = grade(user, accepted)

    if correct:
        print(clr("  ✓ 正確！", G))
        score += 1
    else:
        if not freeform:
            print(clr("  ✗ 錯誤", R))
            print(clr(f"  正確答案：{accepted[0]}", Y))
            if len(accepted) > 1:
                print(clr(f"  （也接受：{' | '.join(accepted[1:])}）", D))
        wrong_list.append(f"{q_tag}({blank_id})")

    return correct


# ─────────────────────────────────────────────────────────────
# Q24：Σ n!  Shared Memory
# ─────────────────────────────────────────────────────────────

Q24_CODE = """
  int main(int argc, char *argv[]) {
      int N = atoi(argv[1]);
      pid_t pid;
      int segment_id;
      int *shared_memory;

      __(A)__                // allocate shared memory segment
      __(B)__                // attach shared memory

      __(C)__                // initialization

      for (__(D)__)          // create N child processes
      {
          __(E)__

          if (__(F)__) {
              fprintf(stderr, "Fork Failed"); exit(-1);
          } else if (__(G)__) {    // child process
              __(H)__              // calculate i! and add to *shared_memory
              __(I)__              // detach and exit
          } else {                 // parent process
              __(J)__
          }
      }

      printf("the result is %d\\n", *shared_memory);
      __(K)__                // detach shared memory
      __(L)__                // remove shared memory segment
      return 0;
  }
"""

def run_q24():
    sep('━')
    print(f"{B}{C}  Q24：Shared Memory — 計算 Σ(n=1 to N) n!{X}  {clr('（12 空格）', Y)}")
    sep('━')
    print(Q24_CODE)

    tag = "Q24"

    ask("A", "__(A)__  // allocate shared memory segment",
        "建立 shared memory segment（函數名稱即可）",
        ["shmget",
         "segment_id = shmget(IPC_PRIVATE, sizeof(int), S_IRUSR | S_IWUSR)"],
        hint="shmget(IPC_PRIVATE, sizeof(int), S_IRUSR | S_IWUSR)",
        q_tag=tag)

    ask("B", "__(B)__  // attach shared memory",
        "附加 shared memory 到 process 位址空間（函數名稱即可）",
        ["shmat",
         "shared_memory = (int *) shmat(segment_id, NULL, 0)"],
        hint="shmat(segment_id, NULL, 0)",
        q_tag=tag)

    ask("C", "*shared_memory = __(C)__;  // initialization",
        "初始化 shared memory 為多少？",
        ["0"],
        q_tag=tag)

    ask("D", "for (__(D)__)  // create N child processes",
        "for 迴圈三個部分（init; condition; increment）",
        ["int i = N; i > 0; i--",
         "i = N; i > 0; i--"],
        hint="從 N 倒數到 1，讓每個 i 對應計算 i!",
        freeform=True, q_tag=tag)

    ask("E", "__(E)__",
        "建立子行程（函數名稱即可）",
        ["fork", "pid = fork()", "pid = fork();"],
        hint="fork()",
        q_tag=tag)

    ask("F", "if (__(F)__) { // fork failed",
        "fork 失敗的錯誤條件",
        ["pid < 0"],
        hint="fork 失敗時回傳值 < 0",
        q_tag=tag)

    ask("G", "else if (__(G)__) { // child process",
        "判斷是否為子行程",
        ["pid == 0"],
        hint="子行程中 fork() 的回傳值為 0",
        q_tag=tag)

    ask("H", "__(H)__  // calculate i! and add to *shared_memory",
        "計算 i! 並累加到 *shared_memory（多行，自評模式）",
        ["int fact = 1;\n    for (int j = i; j > 0; j--) fact *= j;\n    *shared_memory += fact;"],
        hint="先算 i!，再 *shared_memory += fact",
        freeform=True, q_tag=tag)

    ask("I", "__(I)__  // detach and exit",
        "子行程：脫離 shared memory 並退出（寫出兩個函數呼叫）",
        ["shmdt(shared_memory); exit(0)",
         "shmdt(shared_memory);\n    exit(0)"],
        hint="shmdt(shared_memory);  exit(0);",
        freeform=True, q_tag=tag)

    ask("J", "__(J)__  // parent waits for child",
        "父行程等待子行程（函數名稱即可）",
        ["wait(NULL)", "wait"],
        hint="防止 race condition",
        q_tag=tag)

    ask("K", "__(K)__  // detach shared memory",
        "父行程脫離 shared memory（函數名稱即可）",
        ["shmdt(shared_memory)", "shmdt"],
        q_tag=tag)

    ask("L", "__(L)__  // remove shared memory segment",
        "刪除 shared memory segment（函數名稱即可）",
        ["shmctl(segment_id, IPC_RMID, NULL)", "shmctl"],
        hint="shmctl 第二個參數為 IPC_RMID",
        q_tag=tag)


# ─────────────────────────────────────────────────────────────
# Q25 / 練習考卷 Q5A：2x + 3y − 5
# ─────────────────────────────────────────────────────────────

Q25_CODE = """
  int main(int argc, char *argv[]) {
      int x = atoi(argv[1]);
      int y = atoi(argv[2]);
      int i;
      pid_t pid;
      const int sh_size = 4;

      int segment_id = __(A)__(IPC_PRIVATE, sh_size, S_IRUSR | S_IWUSR);
      int *shared_memory = (int *) __(B)__(segment_id, NULL, 0);

      *shared_memory = __(C)__;   // initialization

      for (i = 2; i > 0; i--) {
          pid = __(D)__();

          if (pid < 0) {
              fprintf(stderr, "Fork Failed"); exit(-1);
          } else if (pid == 0) {   // child
              if (i == 2) *shared_memory += __(E)__;  // compute x term
              if (i == 1) *shared_memory += __(F)__;  // compute y term
              shmdt(shared_memory);
              exit(0);
          } else {                  // parent
              __(G)__(NULL);
          }
      }

      *shared_memory -= 5;
      printf("the result is %d\\n", *shared_memory);
      shmdt(shared_memory);
      __(H)__(segment_id, IPC_RMID, NULL);
      return 0;
  }
"""

def run_q25():
    sep('━')
    print(f"{B}{C}  Q25 / 練習 Q5A：Shared Memory — 計算 2x + 3y − 5{X}  {clr('（8 空格）', Y)}")
    sep('━')
    print(Q25_CODE)

    tag = "Q25"

    ask("A", "int segment_id = __(A)__(IPC_PRIVATE, sh_size, S_IRUSR | S_IWUSR);",
        "建立 shared memory segment 的函數名稱",
        ["shmget"], q_tag=tag)

    ask("B", "int *shared_memory = (int *) __(B)__(segment_id, NULL, 0);",
        "附加 shared memory 的函數名稱",
        ["shmat"], q_tag=tag)

    ask("C", "*shared_memory = __(C)__;  // initialization",
        "初始化 shared memory 的值",
        ["0"], q_tag=tag)

    ask("D", "pid = __(D)__();",
        "建立子行程的函數名稱",
        ["fork"], q_tag=tag)

    ask("E", "if (i == 2) *shared_memory += __(E)__;  // x term",
        "i==2 時，計算 x 項並填入表達式",
        ["2 * x", "2*x"],
        hint="計算 2x",
        q_tag=tag)

    ask("F", "if (i == 1) *shared_memory += __(F)__;  // y term",
        "i==1 時，計算 y 項並填入表達式",
        ["3 * y", "3*y"],
        hint="計算 3y",
        q_tag=tag)

    ask("G", "__(G)__(NULL);  // parent waits",
        "父行程等待子行程的函數名稱",
        ["wait"], q_tag=tag)

    ask("H", "__(H)__(segment_id, IPC_RMID, NULL);",
        "移除 shared memory segment 的函數名稱",
        ["shmctl"],
        hint="control shared memory → IPC_RMID",
        q_tag=tag)


# ─────────────────────────────────────────────────────────────
# Q26 / 練習考卷 Q5B：Shell Interface
# ─────────────────────────────────────────────────────────────

Q26_CODE = """
  int main(void) {
      char inputBuffer[80];
      bool background;

      while (cin >> inputBuffer) {
          cout << endl << " COMMAND->";
          pid_t pid;

          // check if command ends with '&'
          if (inputBuffer[strlen(inputBuffer)-1] == '&') {
              background = __(A)__;         // command ends with '&'
              inputBuffer[strlen(inputBuffer)-1] = '\\0';
          } else {
              background = __(B)__;         // no '&'
          }

          // fork a child process
          pid = __(C)__();

          if (pid == 0) {
              // child: execute the command
              __(D)__(inputBuffer);
          } else if (pid > 0) {
              // parent
              if (background == __(E)__)
                  __(F)__(NULL);            // wait for foreground child
          }
      }
      return 0;
  }
"""

def run_q26():
    sep('━')
    print(f"{B}{C}  Q26 / 練習 Q5B：Shell Interface Program{X}  {clr('（6 空格）', Y)}")
    sep('━')
    print(Q26_CODE)

    tag = "Q26"

    ask("A", "background = __(A)__;  // command ends with '&'",
        "指令以 '&' 結尾，background 應設為？",
        ["true"],
        hint="是否在背景執行？→ true / false",
        q_tag=tag)

    ask("B", "background = __(B)__;  // no '&'",
        "指令沒有 '&'，background 應設為？",
        ["false"], q_tag=tag)

    ask("C", "pid = __(C)__();",
        "建立子行程的函數名稱",
        ["fork"], q_tag=tag)

    ask("D", "__(D)__(inputBuffer);  // child executes command",
        "子行程執行指令的函數名稱（exec 家族均可）",
        ["execlp", "execvp", "execl", "execv", "exec"],
        hint="exec 家族：execlp / execvp / ...",
        q_tag=tag)

    ask("E", "if (background == __(E)__)",
        "什麼條件下父行程要呼叫 wait？（前景執行）",
        ["false"],
        hint="background 為何值表示前景？",
        q_tag=tag)

    ask("F", "__(F)__(NULL);  // wait for foreground child",
        "父行程等待子行程的函數名稱",
        ["wait"], q_tag=tag)


# ─────────────────────────────────────────────────────────────
# 主程式
# ─────────────────────────────────────────────────────────────

MENU = f"""
{B}{C}{'━'*62}{X}
{B}{C}  OS 程式填空互動測驗{X}
{B}{C}{'━'*62}{X}

  {B}1.{X} Q24 — Shared Memory: Σ n!       {clr('(12 空格，含自評)', D)}
  {B}2.{X} Q25 — Shared Memory: 2x+3y−5   {clr('(8 空格)', D)}
  {B}3.{X} Q26 — Shell Interface           {clr('(6 空格)', D)}
  {B}4.{X} 全部（Q24 + Q25 + Q26）

"""

def main():
    print(MENU)
    choice = input("  選擇 (1/2/3/4) > ").strip()

    runners = {
        '1': [run_q24],
        '2': [run_q25],
        '3': [run_q26],
        '4': [run_q24, run_q25, run_q26],
    }

    if choice not in runners:
        print(clr("  無效選擇，結束。", R))
        sys.exit(1)

    for fn in runners[choice]:
        fn()

    # ── 結果總結 ──────────────────────────────────────────────
    print("\n")
    sep('━')
    print(f"{B}  最終成績：{score} / {total} 分{X}", end="  ")
    pct = score / total * 100 if total > 0 else 0

    if pct >= 85:
        bar = clr(f"({pct:.0f}%)  ★ 優秀！", G)
    elif pct >= 65:
        bar = clr(f"({pct:.0f}%)  還不錯", Y)
    else:
        bar = clr(f"({pct:.0f}%)  需要多練習", R)
    print(bar)

    if wrong_list:
        print(clr(f"\n  答錯的空格：{', '.join(wrong_list)}", R))
    else:
        print(clr("\n  全部答對！", G))
    sep('━')
    print()


if __name__ == "__main__":
    main()
