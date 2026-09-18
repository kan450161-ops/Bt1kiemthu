"""
Chương trình kiểm tra và phân loại tam giác.
Chuyển đổi (convert) từ project C# WinForms gốc: Tamgiac_Softwaretesting
(WindowsFormsApplication1 / Form1.cs)

Logic được giữ nguyên 1-1 so với bản gốc, bao gồm cả trường hợp đặc biệt
(3, 4, 5) -> "tam giac thuong" thay vì "Vuong" (giữ lại vì đây có vẻ là
một lỗi (bug) cố ý được cài vào để phục vụ bài tập kiểm thử phần mềm -
Software Testing / Boundary Value Analysis).
"""

import tkinter as tk
from tkinter import ttk


def classify_triangle(a: int, b: int, c: int) -> str:
    """
    Phân loại tam giác dựa trên 3 cạnh a, b, c.
    Giữ nguyên toàn bộ logic (kể cả bug) từ bản C# gốc.
    """
    # Điều kiện hợp lệ của từng cạnh (giống bản C# gốc)
    if a < 3 or a > 100 or b < 4 or b > 200 or c < 5 or c > 300:
        return "Invalid"

    # Kiểm tra bất đẳng thức tam giác
    if a >= b + c or b >= a + c or c >= a + b:
        return "Khong la tam giac"

    # Tam giác đều
    if a == b and a == c:
        return "Deu"

    # Tam giác cân
    if a == b or b == c or c == a:
        return "Can"

    # Tam giác vuông (Pythagoras)
    if a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
        # Trường hợp đặc biệt (3,4,5) - giữ nguyên hành vi (bug) của bản gốc
        if a == 3 and b == 4 and c == 5:
            return "tam giac thuong"
        else:
            return "Vuong"

    # Tam giác thường
    return "Tam giac thuong"


class TriangleApp(tk.Tk):
    """Giao diện tương đương Form1 trong bản C# WinForms gốc."""

    def __init__(self):
        super().__init__()
        self.title("Form1")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        # ----- Cạnh a -----
        ttk.Label(self, text="Canh a[3,100]").grid(row=0, column=0, sticky="w", pady=5)
        self.txta = ttk.Entry(self, width=20)
        self.txta.grid(row=0, column=1, pady=5, padx=(10, 0))

        # ----- Cạnh b -----
        ttk.Label(self, text="Canh b[4,200]").grid(row=1, column=0, sticky="w", pady=5)
        self.txtb = ttk.Entry(self, width=20)
        self.txtb.grid(row=1, column=1, pady=5, padx=(10, 0))

        # ----- Cạnh c -----
        ttk.Label(self, text="Canh c[5,300]").grid(row=2, column=0, sticky="w", pady=5)
        self.txtc = ttk.Entry(self, width=20)
        self.txtc.grid(row=2, column=1, pady=5, padx=(10, 0))

        # ----- Nút Check -----
        self.btnChk = ttk.Button(self, text="Check", command=self.btnChk_Click)
        self.btnChk.grid(row=3, column=0, columnspan=2, pady=10)

        # ----- Kết quả -----
        ttk.Label(self, text="Ket qua:").grid(row=4, column=0, sticky="w", pady=5)
        self.txtkq = ttk.Entry(self, width=20, state="readonly")
        self.txtkq.grid(row=4, column=1, pady=5, padx=(10, 0))

    def _set_result(self, text: str):
        self.txtkq.configure(state="normal")
        self.txtkq.delete(0, tk.END)
        self.txtkq.insert(0, text)
        self.txtkq.configure(state="readonly")

    def btnChk_Click(self):
        try:
            a = int(self.txta.get())
            b = int(self.txtb.get())
            c = int(self.txtc.get())
        except ValueError:
            # Trong bản C# gốc, int.Parse lỗi sẽ ném exception
            # (FormatException) khi ô nhập không phải số nguyên.
            self._set_result("Invalid")
            return

        result = classify_triangle(a, b, c)
        self._set_result(result)


if __name__ == "__main__":
    app = TriangleApp()
    app.mainloop()
