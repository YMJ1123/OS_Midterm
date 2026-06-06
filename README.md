# OS Review Materials (Operating Systems)

作業系統期中與期末複習資料整理。期中範圍以 Ch1-Ch5 為主；期末範圍為 **Ch5 投影片第 16 頁開始到 Ch9**。

## Quick Start

- 期中互動複習：開啟 `review.html`
- 期中英文版互動複習：開啟 `review_en.html`
- 期末互動複習：開啟 `review_final.html`
- 期末考古題：閱讀 `期末考古題彙整.md` 或 `期末考古題彙整.pdf`
- 期末解答：閱讀 `期末考古題解答.md` 或 `期末考古題解答.pdf`

互動 HTML 都可以直接用瀏覽器開啟，不需要另外架 server。

## 期末複習資料

| File | Description |
|------|-------------|
| `review_final.html` | 期末互動式複習網頁，涵蓋 Ch5-Ch9 |
| `期末考古題彙整.md` / `.pdf` | 2011-2016 期末考古題彙整，已依題型、年份、章節與主題標註 |
| `期末考古題解答.md` / `.pdf` | 期末考古題詳解，包含甘特圖、銀行家演算法、頁面置換與同步程式填空 |
| `期末複習講義.md` | Ch5-Ch9 複習講義、常考重點、比較表與易錯提醒 |

### 期末互動 HTML 功能

- Ch5-Ch9 各章重點整理
- 銀行家演算法互動演算
- Optimal vs LRU 頁面置換模擬
- 閃卡複習
- 歷屆題型改編測驗與詳解

### 期末重點主題

- **Ch5 CPU Scheduling**：Multilevel Feedback Queue、Waiting Time、Turnaround Time、Load Balancing、Little's Formula、Starvation / Aging
- **Ch6 Process Synchronization**：Critical Section、Peterson's Solution、TestAndSet、Semaphores、Readers-Writers、Producer-Consumer、Monitors
- **Ch7 Deadlocks**：Four Necessary Conditions、Safe / Unsafe State、Banker's Algorithm、Deadlock Prevention / Avoidance
- **Ch8 Main Memory**：Address Binding、Paging、Page Table Size、TLB、Hierarchical Paging、Compaction
- **Ch9 Virtual Memory**：Demand Paging、Page Fault Handling、Page Replacement、Optimal / LRU、Thrashing、Working Set

## 期中複習資料

| File | Description |
|------|-------------|
| `review.html` | 期中互動式複習網頁（中文） |
| `review_en.html` | 期中互動式複習網頁（英文） |
| `複習筆記.md` | 期中複習筆記 |
| `考古題彙整.md` / `.pdf` | 期中考古題彙整 |
| `考古題解答.md` / `.pdf` | 期中考古題解答 |
| `歷屆考題與解答.md` | 歷屆題目與解答整理 |
| `練習考卷.md` | 練習考卷 |
| `練習考卷_答案.md` / `.pdf` | 練習考卷答案 |
| `總複習作答紀錄.md` | 總複習互動問答紀錄與回饋 |

### 期中重點主題

- **Interrupts**：Interrupt vector、interrupt-driven I/O、busy waiting
- **System Calls**：API、software interrupt、dual mode、system call table
- **Processes**：process states、fork / exec / wait、shared memory
- **Threads**：Many-to-One、One-to-One、Many-to-Many、Scheduler Activations、LWP
- **CPU Scheduling**：FCFS、SJF、Priority、Round-Robin、Multilevel Feedback Queue

## Slides And Source Exams

| File | Topic |
|------|-------|
| `ch05.pdf` | CPU Scheduling |
| `ch06.pdf` | Process Synchronization |
| `ch07 (2).pdf` | Deadlocks |
| `ch08_lo.pdf` | Main Memory |
| `ch09_lo.pdf` | Virtual Memory |
| `2011final.pdf` - `2016final.pdf` | 歷屆期末考原始 PDF |

## Suggested Study Flow

1. 先讀 `期末複習講義.md` 建立 Ch5-Ch9 架構。
2. 用 `review_final.html` 練銀行家演算法、頁面置換與閃卡。
3. 讀 `期末考古題彙整.md`，確認每題對應章節與主題。
4. 對照 `期末考古題解答.md` 檢查計算題與證明題寫法。
