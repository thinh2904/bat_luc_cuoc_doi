import find_url
import save_url


start_url = input('Người anh em cho xin cái địa chỉ: ')
max = int(input('Số trang cần tìm: '))
url_list = find_url.find_url(start_url, start_url)
history = find_url.find_next_url(url_list, start_url, max)
save_url.new_folder(input('Tên thư mục lưu: '))
save_url.save_all_file(history, max)