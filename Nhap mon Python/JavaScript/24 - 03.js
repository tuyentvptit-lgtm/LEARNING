let mang = [1, 2, 3, 4, 5]
mang.forEach((Element, index, array) =>{ //không trả về mảng mới, không thay đổi giá trị mảng ban đầu
    // Thực hiện hành động với từng phần tử ở đây
})

//map(): tạo mảng mới = cách tùy chỉnh mảng khác
let a = mang.map((e, i) => {
     return e = e + 1
})

//filter(): tạo mảng mới dựa trên các items từ bảng cũ qua 1 số điều kiện nhất định
let b = mang.filter((e, i) => {
    // Điều kiện ở đây
    if(e > 2)
    return True //Luôn return ra True or False
})
let tuoi = 18
if (tuoi >= 18){
    console.log ('du tuoi di tu');
}