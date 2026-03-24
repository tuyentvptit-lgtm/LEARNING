let mang = [1, 2, 3, 4, 5]
mang.forEach((Element, index, array) =>{ //không trả về mảng mới, không thay đổi giá trị mảng ban đầu
    // Thực hiện hành động với từng phần tử ở đây
})

//map(): tạo mảng mới = cách tùy chỉnh mảng khác
let a = mang.map((e, i) => {
    e = e + 1
})