# Food_Distribution
Nhà vua một nước muốn phân phát đồ ăn cho người dân các tỉnh. Giả sử có n tỉnh được đánh dấu từ 0 đến n - 1. Nhà vua phân phát đồ ăn k lần. Mỗi lần từ tỉnh được đánh dấu thứ x tới tỉnh được đánh dấu thứ y, mỗi tỉnh được phát z kg đồ ăn. Cho một ma trận chứa thông tin về các lần phân phát, với mỗi mảng con trong ma trận có ba phần tử lần lượt tương ứng với x, y, z. Hãy cho biết sau khi phân phát, mỗi tỉnh được đánh dấu từ 0 đến n - 1 lần lượt sẽ có bao nhiêu kg đồ ăn. Trả về mảng chứa các thông tin đó.

Ví dụ:

Với n = 5, k = 2
Và ma trận chứa thông tin các lần phân chia là:
food = [[1, 3, 3],
        [0, 1, 1]]
Ta có: x0 = 1, y0 = 3, z0 = 3
Sau lần phân phát thứ nhất, số kilogram đồ ăn của các tỉnh được xác định theo mảng: [0, 3, 3, 3, 0]
Ta có: x1 = 0, y1 = 1, z1 = 1
Sau lần phân phát thứ hai, số kilogram đồ ăn của các tỉnh được xác định theo mảng: [1, 4, 3, 3, 0]
Vậy đáp án của hàm distributeFood sẽ là [1, 4, 3, 3, 0]
Với n = 3, k = 1 và ma trận chứa thông tin các lần phân chia là: food = [[1, 1, 1]] đáp án của hàm distributeFood sẽ là [0, 1, 0]
