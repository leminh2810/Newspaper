📰 Innovation Newsletter Automation

Innovation Newsletter là dự án Python tự động thu thập – tóm tắt – gửi bản tin công nghệ hàng tuần qua email.
Hệ thống được thiết kế để giúp người dùng dễ dàng tạo các bản tin (newsletter) cập nhật các tin tức nổi bật trong lĩnh vực công nghệ, AI, và đổi mới sáng tạo, sau đó gửi đến danh sách người nhận thông qua Gmail SMTP.

⚙️ Cấu trúc dự án
project/
│
├── newsletter.py         # Gửi bản tin HTML qua email (SMTP Gmail)
├── summary.py            # Thu thập và tóm tắt nội dung bài viết (web scraping)
├── final_newsletter_1.ipynb
├── final_newsletter_2.ipynb
├── final_newsletter_1_qwen.ipynb
├── craw.ipynb            # Notebook thu thập tin tự động
├── test_api_qwen.ipynb   # Notebook thử nghiệm API Qwen / OpenAI
├── test_text2speech.ipynb # Chuyển văn bản newsletter sang giọng nói
├── output_2.mp3          # File audio đọc bản tin
└── v2_tech_newsletter.html # File HTML bản tin chính

🚀 Tính năng chính
1. Thu thập tin tức tự động (summary.py, craw.ipynb)

Sử dụng thư viện requests và BeautifulSoup để lấy nội dung từ các trang tin (VD: TechCrunch, VentureBeat, The Verge…).

Tự động trích xuất tiêu đề và đoạn nội dung.

Hỗ trợ lưu nội dung thô hoặc xuất ra dạng JSON để tái sử dụng.

2. Tóm tắt bằng AI (final_newsletter_*.ipynb)

Dùng API của OpenAI/Qwen để sinh phần tóm tắt, phân tích và biên tập bản tin.

Tạo ra nội dung súc tích, dễ đọc, có thể tùy chỉnh theo chuyên mục: AI, fintech, startup, v.v.

Hỗ trợ định dạng HTML với bố cục chuyên nghiệp, gồm tiêu đề, đoạn mô tả, liên kết nguồn, và ảnh minh họa.

3. Gửi bản tin qua email (newsletter.py)

Gửi bản tin HTML tự động qua Gmail SMTP.

Hỗ trợ UTF-8 encoding cho nội dung tiếng Việt.

Tùy chỉnh tên người gửi và chủ đề thư.

Bảo mật bằng App Password của Gmail (thay cho mật khẩu tài khoản thật).

4. Chuyển bản tin thành giọng nói (test_text2speech.ipynb)

Sử dụng API text-to-speech (OpenAI hoặc Qwen) để tạo file .mp3 đọc toàn bộ nội dung bản tin.

Phù hợp cho podcast hoặc bản tin âm thanh hàng tuần.

🧠 Quy trình hoạt động

Crawling: Lấy bài viết từ các trang web tin tức công nghệ.

Summarization: Dùng mô hình ngôn ngữ lớn (LLM) để tóm tắt và biên tập.

HTML Rendering: Xuất bản tin sang định dạng HTML đẹp mắt.

Email Sending: Gửi bản tin đến người nhận qua Gmail.

(Tùy chọn) Text-to-Speech: Tạo bản đọc audio .mp3.

🧩 Cài đặt & Cấu hình
Yêu cầu môi trường
pip install requests beautifulsoup4 openai smtplib

Cấu hình biến gửi email

Trong file newsletter.py, thay thế bằng thông tin của bạn:

sender_email = "youremail@gmail.com"
sender_password = "your_app_password"  # Mật khẩu ứng dụng Gmail
recipient_email = "recipient@example.com"


⚠️ Lưu ý: Không dùng mật khẩu thật — chỉ dùng App Password do Gmail cung cấp.

📨 Cách sử dụng
✉️ Gửi bản tin
python newsletter.py

🕸️ Thu thập và tóm tắt bài viết
python summary.py

🎧 Tạo bản tin giọng nói

Chạy notebook test_text2speech.ipynb để tạo file âm thanh .mp3.

📂 Ví dụ kết quả

File HTML: v2_tech_newsletter.html

Email preview:

Subject: Innovation Insights Newsletter
From: Innovation Newsletter <youremail@gmail.com>
To: Recipient <recipient@example.com>


Hiển thị bản tin HTML đẹp, sẵn sàng chia sẻ.

File audio: output_2.mp3 – bản đọc toàn bộ nội dung newsletter.

🔒 Bảo mật

Không lưu mật khẩu thật trong code.

Không chia sẻ file .py chứa thông tin xác thực.

Có thể mở rộng thêm file .env để lưu biến môi trường an toàn.
