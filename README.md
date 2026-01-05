You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 🧠 Tư duy giải thuật

 Ý tưởng chính
- Phép nhân -1 cho hai phần tử liền kề có thể di chuyển dấu âm trong ma trận
- Nếu số lượng số âm là chẵn: có thể biến tất cả thành số dương
- Nếu số lượng số âm là lẻ: có thể biến tất cả trừ một số thành dương, số âm còn lại nên là số có giá trị tuyệt đối nhỏ nhất

 Thuật toán
1. Tính tổng giá trị tuyệt đối của tất cả phần tử
2. Đếm số lượng số âm
3. Tìm giá trị tuyệt đối nhỏ nhất
4. Nếu số âm lẻ: `tổng = tổng - 2 * min_abs`

 Độ phức tạp
- **Thời gian:** O(n²) - duyệt qua ma trận một lần
- **Không gian:** O(1) - chỉ sử dụng biến đếm
