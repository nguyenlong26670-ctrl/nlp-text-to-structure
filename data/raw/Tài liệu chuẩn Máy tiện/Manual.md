# Chương 1: Thông tin chung \& Cảnh báo an toàn

> ⚠️ \\\*\\\*CẢNH BÁO TỔNG QUAN:\\\*\\\* Chương này chứa các thông tin thiết yếu mang tính pháp lý và kỹ thuật liên quan trực tiếp đến an toàn tính mạng của người vận hành, cũng như việc bảo vệ tài sản, thiết bị. BẮT BUỘC toàn bộ nhân viên vận hành, kỹ thuật viên bảo dưỡng và kỹ sư sửa chữa phải đọc, hiểu thấu đáo và tuân thủ nghiêm ngặt các quy định trước khi thực hiện bất kỳ thao tác nào trên máy tiện CNC-L200. Nhà sản xuất tuyên bố miễn trừ mọi trách nhiệm pháp lý đối với các thương tích cá nhân, tử vong hoặc hư hỏng thiết bị phát sinh do sự sơ suất, cố ý làm trái hoặc không tuân thủ các quy định an toàn được nêu trong tài liệu này.

## 1.1. Quy định an toàn lao động (LOTO - Lockout/Tagout)

Quy trình Lockout/Tagout (LOTO - Khóa và Gắn thẻ) là tiêu chuẩn an toàn công nghiệp cốt lõi (tuân thủ tiêu chuẩn ISO 14118 và OSHA 29 CFR 1910.147). LOTO được thiết kế nhằm kiểm soát triệt để các nguồn năng lượng nguy hiểm, ngăn ngừa việc máy CNC-L200 khởi động ngoài ý muốn hoặc đột ngột giải phóng năng lượng tích tụ trong quá trình can thiệp kỹ thuật (bảo trì, sửa chữa, vệ sinh sâu, hoặc hiệu chỉnh thiết bị).

Đối với dòng máy tiện CNC-L200, sự phức tạp về cơ điện tử yêu cầu quy trình này phải cách ly hoàn toàn các nguồn năng lượng chính và các năng lượng tiềm tàng đi kèm:

1. **Năng lượng điện:** Nguồn cấp chính 3 pha 380VAC/415VAC (tần số 50Hz/60Hz), dòng điện điều khiển 24VDC, và năng lượng tích tụ trong các tụ điện DC Bus của Servo Drive/Spindle Drive.
2. **Năng lượng khí nén:** Áp suất cung cấp từ nhà máy (thông thường từ 0.6 - 0.8 MPa), lưu trữ trong các bình tích áp, bộ lọc FRL và hệ thống đường ống nội bộ.
3. **Năng lượng thủy lực:** Áp suất cao (từ 3.5 - 6.0 MPa) tạo ra bởi Trạm nguồn thủy lực (Hydraulic Power Unit - HPU) dùng để duy trì lực kẹp mâm cặp, khóa đài dao và di chuyển ụ động.
4. **Hệ thống dung dịch làm mát:** Áp suất và dung dịch tồn dư trong đường ống và bơm tưới nguội.

### 1.1.1. Quy trình 5 bước cách ly năng lượng chuẩn trên CNC-L200

Quy trình LOTO phải và chỉ được thực hiện bởi nhân sự đã qua đào tạo chuyên sâu và được cấp quyền (Authorized Personnel). Việc bỏ qua, làm tắt hoặc làm sai lệch bất kỳ bước nào dưới đây đều cấu thành vi phạm an toàn nghiêm trọng, có thể dẫn đến tai nạn lao động đặc biệt nghiêm trọng.

**Bước 1: Chuẩn bị ngắt năng lượng (Preparation for Shutdown)**

* **Nhận diện:** Đọc kỹ sơ đồ cách ly năng lượng (Energy Isolation Diagram) đính kèm trên cửa tủ điện máy CNC-L200. Xác định chính xác vị trí của cầu dao tổng (Main Disconnect Switch), van ngắt khí nén chính (Main Pneumatic Valve), van xả áp thủy lực và van dung dịch làm mát.
* **Phân tích rủi ro:** Đánh giá các công việc sắp thực hiện để dự trù các rủi ro phát sinh (ví dụ: tháo đài dao có thể dẫn đến rớt cụm do mất trọng tâm).
* **Thông báo (Notification):** Cảnh báo bằng lời nói và biển báo cho toàn bộ nhân sự vận hành lân cận, tổ trưởng ca sản xuất về việc máy CNC-L200 chuẩn bị bị cô lập. Khu vực làm việc phải được chăng dây hoặc đặt rào chắn an toàn bán kính tối thiểu 1.5 mét xung quanh máy.

**Bước 2: Tắt máy có kiểm soát (Controlled Shutdown)**

* Tuyệt đối không sử dụng Nút Dừng Khẩn Cấp (E-Stop) như một phương pháp tắt máy thông thường để bắt đầu LOTO, trừ trường hợp khẩn cấp.
* Đưa tất cả các trục (Trục X, Trục Z, Trục C nếu có) về vị trí gốc máy (Machine Zero Return / Reference Point) để triệt tiêu các ứng suất cơ học trên các trục vít me bi (Ball screw).
* Đảm bảo trục chính (Spindle) đã dừng hoàn toàn (0 RPM). Phát lệnh M05 (Dừng trục chính) và M09 (Tắt dung dịch làm mát) trên bảng MDI.
* Tháo gỡ toàn bộ phôi liệu đang kẹp trên mâm cặp và dao cụ đang ở vị trí chờ (nếu quá trình bảo dưỡng yêu cầu can thiệp vào các bộ phận này).
* Lần lượt tắt nguồn hệ thống điều khiển (NC Power OFF) và sau đó là nguồn máy (Machine Power OFF).

**Bước 3: Cô lập và ngắt nguồn năng lượng (Isolation)**

* **Hệ thống Điện:** Di chuyển ra phía sau máy, gạt Cầu dao cách ly tổng (Main Disconnect Breaker) trên vỏ tủ điện về vị trí "OFF" (O). Đồng thời ngắt CB của hệ thống bơm dung dịch làm mát.
* **Hệ thống Khí nén:** Định vị cụm FRL (Filter-Regulator-Lubricator) thường nằm ở hông máy. Vặn van trượt cấp khí chính (Sliding Valve) sang vị trí đóng để ngắt hoàn toàn nguồn khí nén từ máy nén khí nhà xưởng vào máy CNC.
* **Hệ thống Thủy lực:** Bơm thủy lực đã ngừng hoạt động khi ngắt điện, tuy nhiên cần xác nhận lại van điều khiển lưu lượng chính đã đóng để ngăn dòng chảy ngược.
* **Hệ thống Làm mát:** Đóng van cấp dung dịch làm mát chính.

**Bước 4: Khóa và Gắn thẻ an toàn (Lockout/Tagout Application)**

* **Sử dụng thiết bị chuẩn:** Sử dụng duy nhất các ổ khóa an toàn chuyên dụng cho công nghiệp (Safety Padlocks) đã được cấp phát cá nhân (Mỗi người 1 ổ, 1 chìa duy nhất, không có chìa sơ cua).
* **Khóa cơ học:**

  * **Điện:** Lắp ngoàm khóa đa khoá (Hasps) vào lỗ khóa trên Cầu dao tổng và bấm ổ khóa của người thực hiện vào.
  * **Khí nén:** Sử dụng cáp khóa (Cable lock) hoặc chụp khóa van (Valve lockout) để khóa cố định van khí nén chính ở vị trí "CLOSED/EXHAUST".
  * **Thủy lực:** Sử dụng cáp khóa hoặc chụp khóa van bi (Ball valve lockout) để khóa van điều khiển lưu lượng chính hoặc van cấp nguồn HPU ở vị trí "ĐÓNG".
* **Gắn thẻ cảnh báo:** Gắn thẻ LOTO (Tag) màu đỏ/trắng, bằng vật liệu chống thấm nước vào cùng vị trí ổ khóa. Thẻ BẮT BUỘC phải ghi rõ các thông tin:

  * "NGUY HIỂM: THIẾT BỊ ĐANG BẢO TRÌ - CẤM ĐÓNG ĐIỆN/MỞ VAN"
  * Họ và tên, mã số nhân viên của người đang thực hiện khóa.
  * Thời gian bắt đầu và thời gian dự kiến kết thúc.
  * Chi tiết liên lạc (Số điện thoại/Bộ phận).

**Bước 5: Triệt tiêu năng lượng tích tụ và Xác minh (Stored Energy Release \& Verification)**

> ⚠️ \\\*\\\*NGUY HIỂM TỬ VONG - ĐIỆN ÁP DƯ \\\& ÁP SUẤT NGẦM:\\\*\\\* Tuyệt đối không được xem nhẹ Bước 5. Năng lượng tích tụ trong các tụ điện của Servo/Spindle Drive có thể giữ điện áp chết người lên đến 600VDC trong nhiều phút sau khi ngắt điện. Áp suất thủy lực bị giam trong các van một chiều có thể tạo ra lực cắt/kẹp lên đến hàng tấn, đủ khả năng cắt đứt các chi thể.

* **Xả năng lượng Điện (Electrical Discharge):** BẮT BUỘC chờ tối thiểu 10 phút sau khi ngắt cầu dao tổng để hệ thống điện trở xả (Brake Resistors) tiêu thụ hết điện áp trên DC Bus. Sau đó, kỹ thuật viên dùng đồng hồ vạn năng (Multimeter chuẩn CAT III/IV) đo trực tiếp tại các đầu cực R-S-T và đầu ra U-V-W của biến tần để xác nhận điện áp < 24VDC. **Trường hợp ngoại lệ:** Nếu sau 10 phút điện áp đo được vẫn lớn hơn 24VDC, CẤM thực hiện thao tác tiếp theo. Yêu cầu chờ thêm 10 phút rồi đo lại; nếu điện áp không giảm, mạch xả có thể đã hỏng. Phải báo ngay cho Kỹ sư trưởng để xử lý sự cố trước khi tiếp tục LOTO.
* **Xả năng lượng Khí nén (Pneumatic Bleed-off):** Kéo vòng xả áp trên cụm FRL hoặc mở van xả đáy bình tích áp khí nén (nếu có). Mở cửa máy, thao tác kích hoạt súng xịt khí (Air gun) bằng tay nhiều lần cho đến khi không còn luồng khí nào thoát ra. Quan sát đồng hồ đo áp suất khí nén (Pressure Gauge) phải chỉ chính xác 0 MPa.
* **Xả năng lượng Thủy lực (Hydraulic Depressurization):** Mở từ từ van xả áp (Bleed Valve) trên trạm nguồn thủy lực HPU. Để xả áp lực kẹp ngàm, hãy sử dụng cờ lê chuyên dụng xoay van cơ khí dự phòng (Manual Override) trên cụm van điện từ (Solenoid Valve) điều khiển mâm cặp/ụ động. Đồng hồ áp suất thủy lực của trạm nguồn và nhánh mâm cặp phải tụt về 0 MPa.
* **Xả hệ thống làm mát:** Mở van xả thủ công tại vòi tưới nguội để đảm bảo không còn áp suất dư và dung dịch tồn đọng trong đường ống.
* **Xác minh cuối (Verification Try-Out):** Đứng ngoài vùng nguy hiểm, nhấn nút Khởi động hệ thống (Power ON) và nút Chạy chu trình (Cycle Start) trên bảng điều khiển. Đảm bảo máy hoàn toàn "chết" - không có đèn báo, không có tiếng động cơ, không có chuyển động. Đưa các công tắc về lại vị trí "OFF" sau khi xác minh.

### 1.1.2. Vùng cấm xâm nhập và Cảnh báo mối nguy cơ học ngầm

Ngay cả khi quy trình LOTO dường như đã được thực hiện, NGHIÊM CẤM mọi hành vi chạm tay trực tiếp, đưa các bộ phận cơ thể vào hoặc tháo rời các cụm chi tiết sau đây nếu chưa có biên bản xác nhận hoàn tất 100% Bước 5 từ kỹ sư trưởng:

* **Cụm trục chính (Spindle) \& Cơ cấu Drawbar:**

  * *Mối nguy:* Động cơ trục chính có thể tích lũy thế năng hoặc điện áp. Khối lượng của cụm mâm cặp kết hợp trục chính rất lớn, lực quán tính có thể làm cụm này tự xoay nếu bị tác động lực nhẹ, gây kẹp/nghiền ngón tay.
* **Mâm cặp thủy lực (Hydraulic Chuck) \& Xylanh thủy lực xoay (Rotary Cylinder):**

  * *Mối nguy:* Hệ thống ngàm kẹp (Jaws) và ống kéo (Drawtube) chịu tác động của áp suất dư hoặc lực căng của lò xo hồi vị (Spring return) bên trong xylanh. Việc tháo ốc vít ngàm kẹp khi chưa xả áp suất nhánh có thể khiến ngàm phóng ra ngoài như một viên đạn hoặc kẹp sập bất ngờ với lực lên đến 30 - 40 kN.
* **Đài dao Servo (Servo Turret) \& Khớp nối răng (Curvic Coupling):**

  * *Mối nguy:* Đài dao ở các vị trí không cân bằng tĩnh, khi mất hoàn toàn năng lượng điện giữ phanh (Motor Brake) hoặc áp suất thủy lực nhả khớp, mâm dao có thể bị rơi tự do (Drop/Unclamp) quay theo chiều trọng lực, gây nguy cơ dập nát tay nếu đang thao tác tháo lắp gá dao (Tool holder).
* **Ụ động (Tailstock) \& Nòng ụ động (Quill):**

  * *Mối nguy:* Nòng ụ động (Quill) được đẩy bằng thủy lực. Nếu có áp suất bẫy (Trapped pressure) giữa van một chiều và xylanh nòng, nòng ụ động có thể lao ra phía trước với lực ép tĩnh lớn khi có va chạm cơ học vào hệ thống van.
* **Cụm vít me bi trục Z/X (Z/X Axis Ballscrews) \& Động cơ Servo:**

  * *Mối nguy:* Với cấu trúc máy tiện trục nghiêng (Slant bed), trục X chịu ảnh hưởng của trọng lực. Dù động cơ trục X có phanh từ vĩnh cửu (Holding Brake), tuyệt đối không chui đầu, tay vào không gian giữa đài dao và mâm cặp. Việc tháo rời động cơ trục X mà không chèn các khối chặn cơ khí (Mechanical Blocks) chống rơi dưới đài dao sẽ dẫn đến sự cố sập đài dao chém vào băng máy.
* **Tủ điện điều khiển (Electrical Cabinet):**

  * *Mối nguy:* Hồ quang điện và điện giật. Ngay cả khi đã ngắt cầu dao tổng, phía **trước** của cầu dao tổng (Line side) nối thẳng lưới điện nhà máy VẪN CÓ ĐIỆN. Chỉ những thợ điện được chứng nhận (Certified Electrician) mới được phép mở tấm ốp bảo vệ trong tủ điện.

## 1.2. Giải thích các nhãn dán cảnh báo trên thân máy (Safety Decals \& Labels)

Hệ thống nhãn dán cảnh báo trên máy tiện CNC-L200 được thiết kế và chế tạo tuân thủ nghiêm ngặt các tiêu chuẩn quốc tế ISO 3864 (Màu sắc và biển báo an toàn) và ISO 7010 (Ký hiệu đồ họa an toàn). Những nhãn dán này đóng vai trò là tuyến phòng thủ đầu tiên, cung cấp thông tin thị giác trực quan về các mối nguy hiểm tiềm tàng không thể loại bỏ hoàn toàn bằng thiết kế cơ khí.

> ⚠️ \\\*\\\*LƯU Ý PHÁP LÝ QUAN TRỌNG:\\\*\\\* Tuyệt đối không được bóc, cạo sửa, che khuất hoặc sơn đè lên bất kỳ nhãn dán an toàn nào. Nhà máy sản xuất yêu cầu bộ phận bảo trì phải thường xuyên kiểm tra tình trạng nhãn dán. Nếu phát hiện nhãn dán bị mờ, rách hoặc bong tróc, BẮT BUỘC phải liên hệ ngay với nhà cung cấp để đặt hàng nhãn dán thay thế (dựa trên Mã số Part Number in ở góc dưới cùng của mỗi nhãn).

Dưới đây là 5 loại nhãn dán an toàn cốt lõi được phân bổ trên thân máy CNC-L200:

### 1.2.1. Nhãn dán Cảnh báo Điện áp cao (High Voltage Warning)

* **Tên cảnh báo:** NGUY HIỂM: ĐIỆN ÁP CAO GÂY CHẾT NGƯỜI (DANGER: LETHAL HIGH VOLTAGE).
* **Hình dáng và màu sắc:** Hình tam giác đều, nền màu vàng phản quang, viền đen dày. Biểu tượng trung tâm là một tia sét màu đen hướng từ trên xuống (chuẩn ISO 7010-W012). Thường đi kèm một biển phụ hình chữ nhật nền đỏ bên dưới với dòng chữ "DANGER - HIGH VOLTAGE".
* **Vị trí dán thực tế:**

  * Cửa mặt trước và mặt sau của tủ điện điều khiển trung tâm.
  * Trên nắp bảo vệ của động cơ trục chính (Spindle Motor) và các động cơ Servo (X/Z Axis).
  * Khu vực trạm biến áp của máy (nếu có lắp đặt biến áp cách ly).
* **Ý nghĩa và rủi ro nếu bỏ qua:** Biển báo này chỉ thị vị trí tồn tại điện áp xoay chiều 3 pha 380V/415V cường độ cao và điện áp một chiều (DC Bus) có thể vọt lên trên 600VDC.

  * *Rủi ro:* Bỏ qua cảnh báo và mở tủ điện mà không có đồ bảo hộ chuyên dụng (găng tay cách điện, thảm cao su) có thể dẫn đến hiện tượng phóng hồ quang điện (Arc Flash) gây mù lòa, bỏng sâu; hoặc giật điện trực tiếp gây rung tâm thất, ngừng tim và tử vong tại chỗ.

### 1.2.2. Nhãn dán Cảnh báo Vướng mắc và Cuốn ép (Entanglement \& Rotating Parts)

* **Tên cảnh báo:** CẢNH BÁO: BỘ PHẬN ĐANG QUAY / NGUY CƠ CUỐN ÉP (WARNING: ROTATING PARTS / ENTANGLEMENT HAZARD).
* **Hình dáng và màu sắc:** Hình tam giác đều, nền vàng, viền đen. Biểu tượng đồ họa là một bàn tay hoặc hình nộm người bị lôi cuốn vào giữa hai bánh răng hoặc cuốn vào một trục đang quay (chuẩn ISO 7010-W025).
* **Vị trí dán thực tế:**

  * Bên ngoài cửa che cụm mâm cặp chính (Main Chuck Guard).
  * Nắp che đai truyền động (Drive Belt Cover) của động cơ trục chính.
  * Khu vực động cơ băng tải phôi (Chip Conveyor Motor).
* **Ý nghĩa và rủi ro nếu bỏ qua:** Máy CNC-L200 sở hữu trục chính có thể đạt tốc độ quay lên tới 4000 vòng/phút (RPM) chỉ trong vài giây. Ở tốc độ này, lực ly tâm và lực quán tính là vô cùng lớn.

  * *Rủi ro:* Việc can thiệp bằng tay không khi trục đang quay, mặc quần áo rộng, không búi tóc gọn gàng, đeo trang sức (dây chuyền, nhẫn) hoặc *tuyệt đối cấm kỵ* - **đeo găng tay sợi/vải trong lúc máy đang vận hành/chạy trục chính** sẽ dẫn đến nguy cơ bị vướng vào mâm cặp. Hậu quả trực tiếp là lột da, gãy nát xương tay, đứt lìa chi, hoặc cơ thể bị kéo mạnh đập vào thành máy gây chấn thương sọ não/tử vong.

### 1.2.3. Nhãn dán Cảnh báo Điểm kẹp dập cơ học (Crushing Hazard / Pinch Point)

* **Tên cảnh báo:** CẢNH BÁO: ĐIỂM KẸP DẬP / NGUY CƠ NGHIỀN NÁT (WARNING: CRUSHING HAZARD / PINCH POINT).
* **Hình dáng và màu sắc:** Hình tam giác đều, nền vàng, viền đen. Biểu tượng cho thấy một bàn tay hoặc chi thể bị ép nát giữa hai khối cơ khí chữ nhật đang tiến lại gần nhau (chuẩn ISO 7010-W024).
* **Vị trí dán thực tế:**

  * Hai bên hông của đài dao Servo (Turret).
  * Dọc theo các tấm che băng trượt (Telescopic Way Covers) của trục Z và trục X.
  * Khu vực nòng của ụ động (Tailstock Quill) tiếp xúc với phôi.
  * Ray trượt của cửa bảo vệ chính (Automatic Front Door - nếu có tuỳ chọn).
* **Ý nghĩa và rủi ro nếu bỏ qua:** Cảnh báo các vị trí mà các cơ cấu máy có khối lượng hàng trăm kilogram di chuyển tương đối với nhau. Tốc độ chạy dao nhanh (Rapid Traverse) của máy có thể đạt 24m/phút - 30m/phút. Lực ép tạo ra bởi động cơ Servo kết hợp vít me bi hoặc áp suất thủy lực của ụ động có thể lên tới vài tấn.

  * *Rủi ro:* Đặt tay, đầu hoặc các dụng cụ (như cờ lê, búa) vào vùng giới hạn (Pinch zone) trong quá trình máy gá dao tự động, chạy JOG hoặc đo bù dao. Rủi ro bao gồm dập nát ngón tay, đứt rời bàn tay, hoặc phá hủy hoàn toàn cụm cơ khí nếu xảy ra va chạm (Crash).

### 1.2.4. Nhãn dán Cảnh báo Văng bắn mảnh vụn (Flying Debris Hazard)

* **Tên cảnh báo:** CẢNH BÁO: MẢNH VĂNG TỐC ĐỘ CAO / BẮT BUỘC ĐEO KÍNH (WARNING: FLYING DEBRIS / EYE PROTECTION REQUIRED).
* **Hình dáng và màu sắc:** Thường là nhãn kép. Một hình tam giác nền vàng viền đen với biểu tượng các mảnh văng hình tia xạ (ISO 7010-W042). Ngay bên cạnh hoặc bên dưới là hình tròn nền xanh dương với biểu tượng khuôn mặt mang kính bảo hộ màu trắng (Lệnh bắt buộc - Mandatory Sign, ISO 7010-M004).
* **Vị trí dán thực tế:**

  * Ngay trên lớp kính cường lực quan sát ở cửa trước của máy (Front Door Viewing Window).
  * Khu vực máng xả phôi (Chip Chute) đổ ra băng tải.
* **Ý nghĩa và rủi ro nếu bỏ qua:** Quá trình tiện kim loại sinh ra các phôi (Chip) sắc bén, nóng đỏ (lên tới hàng trăm độ C). Ngoài ra, nguy cơ tiềm tàng là mảnh dao cụ (Insert) bị vỡ do quá tải, hoặc phôi liệu bị tuột khỏi mâm cặp văng ra do gá kẹp không đủ lực tĩnh hoặc lực ly tâm quá lớn.

  * *Rủi ro:* Các vật thể này bay ra với vận tốc tương đương một viên đạn. Bỏ qua cảnh báo bằng cách mở cửa khi máy đang gia công hoặc không đeo kính bảo hộ tiêu chuẩn ANSI Z87.1 sẽ dẫn đến hậu quả bị mảnh vụn găm sâu vào da thịt, xuyên thủng nhãn cầu gây mù lòa vĩnh viễn, hoặc chấn thương sọ não hở.

### 1.2.5. Nhãn dán Cảnh báo Bề mặt Nhiệt độ cao (Hot Surface Warning)

* **Tên cảnh báo:** THẬN TRỌNG: BỀ MẶT NÓNG / NGUY CƠ BỎNG (CAUTION: HOT SURFACE / BURN HAZARD).
* **Hình dáng và màu sắc:** Hình tam giác đều, nền vàng, viền đen. Biểu tượng là một bề mặt phẳng nằm ngang với các vạch sóng nhiệt (chỉ hơi nóng) bốc lên phía trên (chuẩn ISO 7010-W017).
* **Vị trí dán thực tế:**

  * Vỏ bọc ngoài của Động cơ trục chính và cụm thân trục chính.
  * Khu vực tản nhiệt (Heat sink) của Tủ điện.
  * Bơm thủy lực và các ống dẫn dầu áp suất cao.
  * Khu vực chứa phôi thải ở đuôi băng tải.
* **Ý nghĩa và rủi ro nếu bỏ qua:** Các bộ phận này chuyển hóa một lượng lớn năng lượng điện và cơ năng thành nhiệt năng trong quá trình gia công liên tục nhiều giờ (Heavy-duty cycle). Nhiệt độ tại động cơ trục chính hoặc các chi tiết ma sát hoàn toàn có thể vượt qua ngưỡng 70°C (158°F). Phôi cắt vừa thoát ra có thể đạt 500°C - 800°C.

  * *Rủi ro:* Chạm tay trần hoặc các bộ phận da hở vào các khu vực này ngay sau khi vừa dừng máy sẽ dẫn đến tổn thương lớp biểu bì, gây bỏng nhiệt cấp độ 2 hoặc cấp độ 3. Bắt buộc phải chờ tối thiểu 30 phút để thiết bị nguội tự nhiên và **bắt buộc sử dụng găng tay chịu nhiệt khi bảo dưỡng các cụm này (chỉ thực hiện thao tác bảo dưỡng sau khi máy đã dừng hoàn toàn và áp dụng thành công LOTO)**.

## 1.3. Yêu cầu về môi trường đặt máy và kết nối hạ tầng (Installation Environment \& Infrastructure Requirements)

Để đảm bảo máy tiện CNC-L200 hoạt động với độ chính xác cao nhất (đạt dung sai theo chuẩn ISO 230-1), kéo dài tuổi thọ hệ thống cơ điện tử và tuân thủ các quy chuẩn an toàn, chủ đầu tư BẮT BUỘC phải chuẩn bị môi trường và hạ tầng lắp đặt đáp ứng nghiêm ngặt các thông số kỹ thuật dưới đây trước khi tiến hành dỡ hàng và định vị máy.

> ⚠️ \\\*\\\*CẢNH BÁO TỪ NHÀ SẢN XUẤT:\\\*\\\* Mọi hư hỏng đối với bo mạch điện tử, sai số gia công cơ khí hoặc sự cố an toàn do việc lắp đặt máy trong điều kiện môi trường, nền móng hoặc nguồn điện không đạt chuẩn sẽ dẫn đến việc \\\*\\\*TỪ CHỐI BẢO HÀNH\\\*\\\* toàn bộ hệ thống.

### 1.3.1. Yêu cầu về môi trường buồng máy (Operating Environment)

Bộ điều khiển CNC (CNC Controller), hệ thống Servo Amplifier và các cảm biến quang học/từ tính trên máy đặc biệt nhạy cảm với sự biến thiên nhiệt độ và hơi ẩm.

* **Nhiệt độ môi trường (Ambient Temperature):**

  * **Khoảng hoạt động cho phép:** $10^\\circ C$ đến $40^\\circ C$ ($50^\\circ F - 104^\\circ F$).
  * **Nhiệt độ tối ưu cho độ chính xác cao:** $20^\\circ C \\pm 2^\\circ C$. Sự thay đổi nhiệt độ đột ngột vượt quá $1^\\circ C$/giờ sẽ gây ra hiện tượng giãn nở nhiệt (Thermal Expansion) không đồng đều trên thân máy đúc và cụm vít me bi, dẫn đến sai lệch kích thước gia công.
* **Độ ẩm tương đối (Relative Humidity - RH):**

  * **Giới hạn cho phép:** $30% - 75%$ (Không đọng sương - Non-condensing).
  * *Mối nguy:* Độ ẩm vượt ngưỡng 75% sẽ gây ra hiện tượng đoản mạch (Short circuit) trên các linh kiện dán (SMD) của bo mạch, oxy hóa các tiếp điểm Relay và rỉ sét các bề mặt kim loại không sơn phủ.
* **Chất lượng không khí:** Không gian đặt máy phải thông thoáng, tuyệt đối tránh các khu vực có chứa khí ăn mòn (Sulfur dioxide, Axit bay hơi) hoặc bụi dẫn điện (Bụi than chì graphite, bụi bột kim loại siêu mịn).

### 1.3.2. Yêu cầu nền móng và chống rung chấn (Foundation \& Anti-Vibration)

Máy tiện CNC-L200 có trọng lượng tĩnh lớn và tạo ra mô-men xoắn cao trong quá trình cắt gọt. Một nền móng không vững chắc sẽ làm thân máy (Machine bed) bị vặn xoắn theo thời gian, phá hủy hoàn toàn hình học cơ sở của máy.

* **Độ cứng và kết cấu nền bê tông:**

  * Sử dụng bê tông cốt thép mác từ **M300 (C30)** trở lên.
  * **Độ dày bê tông tối thiểu:** $\\ge 300mm$ ($12 \\text{ inches}$). Cốt thép phải được đan tối thiểu hai lớp phi 12 (D12).
  * Khả năng chịu tải bề mặt BẮT BUỘC phải lớn hơn $5000 \\text{ kg/m}^2$.
  * Độ phẳng bề mặt trước khi đổ lớp vữa tự san phẳng (Epoxy) không được vượt quá độ võng $5mm$ trên chiều dài $3\\text{m}$.
* **Cách ly rung chấn (Vibration Isolation):**

  * *Mối nguy:* Rung động từ các thiết bị xung quanh như máy dập (Punch press), búa máy (Drop forge), máy mài cỡ lớn hoặc trạm nén khí trung tâm sẽ truyền qua nền đất và làm bề mặt tiện bị lỗi "vảy cá" (Chatter marks).
  * *Giải pháp:* Nếu trong xưởng có nguồn phát rung chấn biên độ lớn (Gia tốc rung $> 0.5 G$), yêu cầu phải đào một mương chống rung (Vibration isolation trench) sâu tối thiểu $600mm$, rộng $100mm$ bao quanh toàn bộ móng máy. Mương này phải được lấp đầy bằng cát khô, mùn cưa hoặc chèn vật liệu đệm cao su Neoprene để triệt tiêu sóng cơ học.
* **Hệ thống thoát nước (Drainage):** Cần thiết kế rãnh thu hồi dầu cắt gọt (Coolant) bị tràn rò rỉ xung quanh bệ máy với độ dốc $1% - 2%$ hướng về hệ thống xử lý nước thải hoặc thùng tách váng dầu (Oil Skimmer) của xưởng.

### 1.3.3. Yêu cầu nguồn điện và hệ thống tiếp địa (Power Supply \& Grounding)

Sự ổn định của lưới điện là yếu tố sống còn để đảm bảo Board điều khiển CNC không bị treo (System Hang) và Spindle Motor không bị suy giảm tuổi thọ do sụt áp/quá áp.

* **Thông số nguồn điện cung cấp (Main Power Supply):**

  * **Điện áp xoay chiều:** 3 Pha 4 Dây (3P+PE), $380\\text{VAC}$ hoặc $415\\text{VAC}$ (Tùy cấu hình máy biến áp).
  * **Tần số:** $50\\text{Hz}$ hoặc $60\\text{Hz}$ ($\\pm 1\\text{Hz}$).
  * **Biến thiên điện áp tối đa (Voltage Fluctuation):** $\\pm 10%$. Nếu điện áp lưới nhà máy thường xuyên trồi sụt vượt ngưỡng này, yêu cầu BẮT BUỘC phải trang bị Bộ ổn áp tự động (AVR - Automatic Voltage Regulator) công suất tối thiểu $30\\text{ kVA}$.
  * **Mất cân bằng pha (Phase Imbalance):** Không được vượt quá $5%$ để tránh cháy cuộn dây động cơ.
* **Hệ thống nối đất tiếp địa (Grounding System):**

> ⚠️ \\\*\\\*NGUY HIỂM TỬ VONG - HỆ THỐNG TIẾP ĐỊA:\\\*\\\* Tuyệt đối không được nối đất máy CNC chung với hệ thống nối đất của kết cấu nhà xưởng, cột thu lôi chống sét hoặc các máy móc công suất lớn khác. Việc nối đất chung có thể dẫn đến hiện tượng nhiễu vòng lặp nối đất (Ground Loop Noise), gây nhiễu loạn tín hiệu Encoder và nguy cơ phóng điện ngược làm chết người vận hành.

* **Tiêu chuẩn cọc tiếp địa:** Máy CNC-L200 phải có một hệ thống cọc tiếp địa bằng đồng (Copper Ground Rod) cắm sâu vào lòng đất ĐỘC LẬP HOÀN TOÀN (Independent Class 3 Grounding).
* **Điện trở nối đất (Grounding Resistance):** Phải được đo lường bằng máy đo điện trở đất chuyên dụng và đạt giá trị $\\le 10 \\Omega$ (Khuyến cáo tối ưu nhất cho hệ thống Servo kỹ thuật số là $< 4 \\Omega$).
* **Dây tiếp địa (PE Wire):** Sử dụng cáp đồng bọc PVC tiết diện tối thiểu $14\\text{ mm}^2$ (AWG 6) nối trực tiếp từ cọc tiếp địa độc lập lên khối nối đất trung tâm (Ground Busbar) bên trong tủ điện CNC.





\# Chương 2: Thông số kỹ thuật (Machine Specifications)



\## 2.1. Kích thước và Trọng lượng (Dimensions \& Weight)



| Thông số | Đơn vị | Giá trị |

| :--- | :--- | :--- |

| Chiều dài tổng thể (không bao gồm băng tải phoi) | mm | 2550 |

| Chiều rộng tổng thể | mm | 1650 |

| Chiều cao tổng thể | mm | 1850 |

| Chiều cao tâm trục chính (tính từ mặt sàn) | mm | 1050 |

| Trọng lượng tịnh (Net Weight) | kg | 4200 |



Máy tiện CNC-L200 được thiết kế trên nền tảng khung bệ đúc nguyên khối từ gang Meehanite chất lượng cao, kết hợp với cấu trúc băng máy nghiêng (Slant bed) 45 độ. Cấu trúc này không chỉ hạ thấp trọng tâm, gia tăng độ cứng vững xoắn mà còn cung cấp khả năng tự nhiên tuyệt vời trong việc dập tắt rung động (vibration damping) sinh ra từ quá trình cắt gọt hạng nặng. Trọng lượng tịnh 4200 kg của cỗ máy đòi hỏi một nền móng bê tông cốt thép đặc biệt, bắt buộc phải đáp ứng khả năng chịu tải tĩnh và động $> 5000 \\text{ kg/m}^2$ như đã quy định tại Chương 1, nhằm triệt tiêu hoàn toàn sự biến dạng cơ học theo thời gian.



Về bố trí không gian nhà xưởng, sơ đồ lắp đặt yêu cầu duy trì khoảng trống tối thiểu (clearance) là 1000 mm ở phía sau, 1500 mm ở phía hông đổ phoi, 1000 mm ở phía trước (vùng vận hành chính) và 1000 mm ở phía hông còn lại của máy. Khoảng không gian chết này là bắt buộc để đảm bảo an toàn tuyệt đối cho kỹ thuật viên khi thực hiện quy trình LOTO (Lockout/Tagout). Cụ thể, khoảng trống phía sau đảm bảo thợ điện có đủ không gian thao tác đóng ngắt cầu dao tổng, thoát hiểm nhanh khi có hồ quang điện, trong khi khoảng trống bên hông và phía trước cho phép tiếp cận an toàn cụm FRL khí nén, bảo dưỡng hệ thống bơm thủy lực và khu vực thao tác mà không vướng vào các vùng rủi ro kẹp dập (Pinch Points).



\## 2.2. Năng lực gia công (Working Capacity)



| Thông số | Đơn vị | Giá trị |

| :--- | :--- | :--- |

| Đường kính tiện qua băng máy (Swing over bed) | mm | 520 |

| Đường kính tiện tối đa (Max turning diameter) | mm | 320 |

| Chiều dài tiện tối đa (Max turning length) | mm | 500 |

| Đường kính phôi lớn nhất qua lỗ trục chính (Bar capacity) | mm | 52 |

| Kích thước mâm cặp tiêu chuẩn (Hydraulic Chuck) | inch | 8 |

| Trọng lượng phôi tối đa (Chỉ kẹp mâm cặp) | kg | 150 |

| Trọng lượng phôi tối đa (Có chống tâm ụ động) | kg | 300 |



Với cấu hình mâm cặp thủy lực 8 inch tiêu chuẩn kết hợp cùng hệ thống trục chính mô-men xoắn cao, CNC-L200 được tối ưu hóa cho các nguyên công cắt gọt hạng nặng (Heavy-duty cutting). Sự kết hợp giữa động cơ công suất lớn và khung bệ Meehanite cho phép máy xử lý mượt mà các loại vật liệu có độ cứng và độ dai cao như thép hợp kim (4140, 4340), thép công cụ hoặc các dòng thép không gỉ (Inox 304, 316) mà không để lại hiện tượng vảy cá (chatter marks) trên bề mặt chi tiết gia công.



Trong quá trình vận hành thực tế, việc gá kẹp các phôi liệu dài đòi hỏi sự tuân thủ nghiêm ngặt các nguyên tắc động lực học để ngăn chặn sự cố văng phôi tốc độ cao. Khi chiều dài phần phôi nhô ra khỏi mặt ngàm mâm cặp vượt quá 3 lần đường kính của nó, bắt buộc phải kích hoạt hệ thống ụ động đẩy bằng nòng thủy lực (Quill) để chống tâm, giảm thiểu lực ly tâm và hiện tượng võng phôi. Đối với các ứng dụng cấp phôi thanh tự động qua lỗ trục chính (đường kính lên đến 52 mm), kỹ thuật viên phải lắp đặt các ống lót trục chính (Spindle Liners) vừa vặn với kích thước phôi nhằm triệt tiêu hiện tượng quật phôi (whipping effect) bên trong nòng trục, bảo vệ hệ thống vòng bi trục chính và loại trừ nguy cơ phôi biến dạng văng bắn ra ngoài.



\## 2.3. Thông số Trục chính (Spindle Specifications)



| Thông số | Đơn vị | Giá trị |

| :--- | :--- | :--- |

| Tốc độ quay lớn nhất (Max Spindle Speed) | Vòng/phút (RPM) | 4000 |

| Công suất động cơ (Liên tục / Định mức 30 phút) | kW | 11 / 15 |

| Mô-men xoắn tối đa (Max Torque) | N.m | 167 |

| Chuẩn mũi trục chính (Spindle Nose) | - | A2-6 |

| Đường kính vòng bi trục chính (Spindle Bearing Dia.) | mm | 100 |



Hệ thống trục chính của CNC-L200 là trái tim của toàn bộ cỗ máy, được dẫn động bằng động cơ AC Spindle hiệu suất cao với công suất định mức 30 phút lên đến 15 kW. Động cơ này cung cấp mô-men xoắn cực đại 167 N.m ở dải tốc độ thấp để phá thô vật liệu, đồng thời duy trì sự ổn định tuyệt đối khi tăng tốc lên mức tối đa 4000 RPM cho nguyên công tiện tinh. Để đối phó với lượng nhiệt năng khổng lồ sinh ra ở tốc độ 4000 RPM, cụm trục chính được bao bọc bởi hệ thống áo nước/dầu làm mát tuần hoàn (Spindle Chiller System) nhằm duy trì độ cân bằng nhiệt, ngăn ngừa sự giãn nở nhiệt làm sai lệch độ đồng tâm của mũi trục chính chuẩn A2-6 và bảo vệ cụm vòng bi tiếp xúc góc siêu chính xác (lớp P4).



Tuy nhiên, việc vận hành trục chính ở dải tốc độ tối đa đi kèm với các mối nguy hiểm tiềm tàng nghiêm trọng liên quan đến lực ly tâm (Centrifugal Force). Như đã được nhấn mạnh tại cảnh báo an toàn ở Chương 1, khi tốc độ trục chính tiệm cận mốc 4000 RPM, lực ly tâm sẽ có xu hướng kéo các ngàm kẹp (Jaws) của mâm cặp thủy lực mở ra, làm suy giảm đáng kể lực kẹp thực tế (Dynamic Grip Force) so với lực kẹp tĩnh ban đầu.



Kỹ sư lập trình và người vận hành tuyệt đối không được thiết lập tốc độ cắt vượt quá tốc độ tối đa cho phép được khắc trên mặt mâm cặp, đồng thời phải tuân thủ nghiêm ngặt giới hạn trọng lượng phôi (150 kg khi kẹp hẫng và 300 kg khi có chống tâm). Việc ngó lơ định luật vật lý này, kết hợp với một phôi liệu có khối lượng lớn không được chống tâm, sẽ biến chi tiết gia công thành một vật thể văng đạn đạo xuyên phá cửa kính cường lực, đe dọa trực tiếp đến sinh mạng nhân sự trong xưởng.



\## 2.4. Thông số Đài dao (Turret) \& Hệ thống truyền động Trục X/Z



| Thông số Đài dao (Turret) | Đơn vị | Giá trị |

| :--- | :--- | :--- |

| Loại đài dao | - | Servo Turret |

| Số vị trí dao (Tool Stations) | Vị trí | 12 |

| Kích thước cán dao vuông (Square Shank) | mm | 25 x 25 |

| Kích thước cán dao tròn (Round/Boring Shank) | mm | Tối đa Ø40 |

| Thời gian chuyển dao (Trạm kế tiếp / Xa nhất) | Giây (s) | 0.2 / 0.6 |



| Thông số Trục X/Z (Axes Specifications) | Đơn vị | Giá trị |

| :--- | :--- | :--- |

| Hành trình trục X (X-Axis Travel) | mm | 175 |

| Hành trình trục Z (Z-Axis Travel) | mm | 520 |

| Tốc độ di chuyển nhanh (Rapid Traverse) - Trục X | m/phút | 24 |

| Tốc độ di chuyển nhanh (Rapid Traverse) - Trục Z | m/phút | 30 |

| Thông số vít me bi (Ball Screw - Cấp C3) | mm | Ø32, Bước ren 10 |



Sự kết hợp giữa động cơ Servo phân độ tốc độ cao và cơ chế khóa đài dao bằng khớp nối răng (Curvic Coupling) 3 mảnh là một kiệt tác thiết kế cơ khí trên CNC-L200. Khi có lệnh gọi dao, mâm dao sẽ được nhả khớp bằng áp suất thủy lực, động cơ Servo ngay lập tức xoay đến vị trí chỉ định với thời gian (Index time) chớp nhoáng 0.2 giây cho trạm kế tiếp. Điểm mấu chốt nằm ở lúc khóa lại: bề mặt các răng xéo của khớp nối Curvic sẽ tự định tâm và ăn khớp hoàn toàn dưới lực ép thủy lực khổng lồ. Cơ chế này loại bỏ mọi độ rơ cơ học (backlash), đảm bảo đài dao chịu tải cắt gọt gián đoạn cực tốt và duy trì độ chính xác lặp lại (Repeatability) ở mức $\\pm 0.002 \\text{ mm}$.



Đối với hệ thống truyền động tuyến tính, các trục X và Z được trang bị vít me bi siêu chính xác cấp C3 (đường kính 32 mm, bước ren 10 mm) liên kết trực tiếp (Direct drive) với động cơ Servo qua khớp nối mềm không độ rơ. Thiết kế này giúp trục X đạt tốc độ di chuyển nhanh 24 m/phút và trục Z lên tới 30 m/phút. Gia tốc lớn và sự triệt tiêu ma sát trượt nhờ các thanh ray dẫn hướng tuyến tính loại con lăn (Roller LM Guideways) giúp giảm tối đa thời gian không gia công (Non-cutting time), tối ưu hóa năng suất sản xuất hàng loạt.



Tuy nhiên, tốc độ di chuyển 30 m/phút (tương đương 500 mm/giây) sinh ra mối nguy cơ học chết người. Ở vận tốc này, bất kỳ sự can thiệp trực tiếp nào của con người vào không gian làm việc khi trục đang di chuyển đều không cho phép thời gian phản xạ để tránh né. Rủi ro kẹp dập cơ học (Crushing Hazard / Pinch Point) giữa đài dao và mâm cặp hoặc ụ động là cực kỳ hiện hữu. Đây là lý do nhà sản xuất nghiêm cấm mọi hành vi vô hiệu hóa (Bypass) công tắc khóa liên động an toàn (Door Interlock) để chạy máy hoặc can thiệp JOG trục khi cửa máy chưa đóng hoàn toàn.



\## 2.5. Thông số Ụ động (Tailstock Specifications)



| Thông số | Đơn vị | Giá trị |

| :--- | :--- | :--- |

| Hành trình thân ụ động (Tailstock Body Travel) | mm | 450 |

| Hành trình nòng ụ động (Quill Stroke) | mm | 80 |

| Đường kính nòng ụ động (Quill Diameter) | mm | 65 |

| Độ côn mũi tâm (Tailstock Taper) | - | MT4 |

| Lực đẩy nòng tối đa (tại 3.5 - 6.0 MPa) | kN | 2.5 - 4.5 |



Thiết kế ụ động của CNC-L200 kết hợp giữa sự vững chãi cơ học và tính linh hoạt của hệ thống thủy lực, chuyên trị các phôi liệu dạng trục có tỉ lệ $L/D$ (Chiều dài/Đường kính) lớn. Khi tiện các chi tiết dài, ma sát và năng lượng cắt gọt sẽ chuyển hóa thành nhiệt năng, làm phôi kim loại giãn nở tuyến tính. Điểm ưu việt của nòng ụ động đẩy bằng thủy lực nằm ở khả năng cung cấp một lực chống tâm hằng số liên tục. Dưới sự điều chỉnh áp suất thủy lực từ 3.5 - 6.0 MPa (tương ứng tạo ra lực đẩy từ 2.5 đến 4.5 kN), nòng ụ động tự động thụt lùi cực vi mô để bù trừ đi độ giãn nở nhiệt của phôi, tránh làm cong võng phôi hoặc phá hủy ổ bi của mũi chống tâm quay (Live Center).



Mặc dù mang lại hiệu năng cao, kỹ thuật viên bảo trì phải cực kỳ thận trọng với nguy cơ tiềm ẩn liên quan đến áp suất bẫy (Trapped pressure) bên trong hệ thống xylanh ụ động. Do được thiết kế tích hợp các van một chiều chống lún (Check valves) nhằm chống rớt nòng khi mất điện đột ngột, áp suất cao vẫn bị giam lỏng giữa van và xylanh ngay cả khi máy đã tắt. Nếu quá trình tháo lắp nòng ụ động hoặc cụm van điều khiển được thực hiện mà không trải qua bước xả áp thủy lực triệt để (như đã quy định tại phần 1.1.1 - LOTO), áp suất bẫy này có thể đột ngột đẩy nòng phóng ra phía trước với lực ép tĩnh lên tới hàng tấn, gây ra tai nạn chấn thương nghiêm trọng cho người bảo dưỡng.



\## 2.6. Yêu cầu Hệ thống Năng lượng \& Môi chất (Power \& Utility Requirements)



| Thông số | Đơn vị | Giá trị |

| :--- | :--- | :--- |

| Tổng công suất điện yêu cầu | kVA | 30 |

| Điện áp cung cấp (Tần số) | - | 3 Pha, 380/415VAC (50/60Hz) |

| Áp suất khí nén đầu vào | MPa | 0.6 - 0.8 |

| Lưu lượng khí nén tiêu thụ | L/phút | \~150 |

| Áp suất vận hành trạm nguồn thủy lực | MPa | 3.5 - 6.0 |

| Dung tích thùng dầu thủy lực | Lít | 40 |

| Dung tích thùng nước làm mát (Coolant) | Lít | 120 |

| Áp suất bơm làm mát (Coolant Pump Pressure) | MPa | 0.3 - 0.5 |

| Lưu lượng bơm làm mát (Coolant Flow Rate) | L/phút | 40 |



Sự vận hành trơn tru và độ bền bỉ của máy tiện CNC-L200 phụ thuộc sống còn vào chất lượng của các nguồn năng lượng chính: Điện, Khí nén, Thủy lực và Môi chất làm mát. Với tổng công suất thiết kế 30 kVA, hệ thống điều khiển NC, các bộ khuếch đại Servo và động cơ Spindle đòi hỏi nguồn điện xoay chiều 3 pha (380VAC hoặc 415VAC) cực kỳ ổn định. Bên cạnh đó, hệ thống khí nén (được cấp ở dải 0.6 - 0.8 MPa) đảm nhận các nhiệm vụ quan trọng như xịt sạch bề mặt đồ gá hay điều khiển chốt cửa an toàn. Nguồn khí nén bắt buộc phải được lọc sạch bụi bẩn và sấy khô hoàn toàn, bởi hơi ẩm xâm nhập vào các van điện từ (Solenoid valves) sẽ gây kẹt lõi van, dẫn đến lỗi tín hiệu không phản hồi trong quá trình gia công tự động.



Hệ thống bơm làm mát cung cấp áp suất 0.3 - 0.5 MPa và lưu lượng 40 L/phút phải được tích hợp chặt chẽ vào quy trình LOTO để đảm bảo triệt tiêu hoàn toàn áp lực bẫy trước khi thực hiện các hoạt động bảo dưỡng.



Quan trọng hơn cả, như đã nhấn mạnh trong Chương 1, hệ thống nối đất tiếp địa (Grounding System) là rào chắn an toàn tối hậu không thể thỏa hiệp. Mạch điện tử số (Digital Servo) cực kỳ nhạy cảm với nhiễu điện từ. Việc đảm bảo điện trở nối đất độc lập $< 10 \\Omega$ không chỉ triệt tiêu hiện tượng nhiễu vòng lặp nối đất (Ground Loop Noise) giúp máy chạy êm ái không mất bước, mà còn dẫn xuất ngay lập tức các dòng rò rỉ điện áp cao (có thể xuất hiện ở động cơ trục chính hoặc biến tần) xuống đất. Bỏ qua tiêu chuẩn tiếp địa này đồng nghĩa với việc mở đường cho các linh kiện đắt tiền bị thiêu rụi bởi điện áp sốc và đẩy người vận hành vào nguy cơ bị điện giật chí mạng khi chạm vào vỏ máy.



# Chương 3: Cấu tạo \& Chức năng các cụm chi tiết

Bảng điều khiển (Control Panel) là giao diện tương tác Người - Máy (HMI) cốt lõi của máy tiện CNC-L200. Đây không chỉ là nơi kỹ thuật viên ban hành các lệnh gia công mà còn là trung tâm giám sát tình trạng hệ thống và kích hoạt các chốt chặn an toàn. Việc hiểu sai lệch hoặc thao tác nhầm lẫn trên bảng điều khiển không chỉ làm hỏng chi tiết gia công mà còn có thể kích hoạt chuỗi tai nạn cơ học đã được cảnh báo.

## 3.1. Giải thích ý nghĩa Bảng điều khiển CNC (Control Panel)

Bảng điều khiển của CNC-L200 được chia thành các phân khu chức năng riêng biệt nhằm tối ưu hóa công thái học và giảm thiểu sai sót do thao tác "mù" của người vận hành. Dưới đây là phân tích kỹ thuật chuyên sâu cho từng cụm.

### 3.1.1. Cụm Nguồn và An toàn (Power \& Safety)

|**Phím / Nút bấm**|**Ký hiệu thường thấy**|**Chức năng cơ bản**|
|-|-|-|
|**NC Power ON/OFF**|Nút bấm (Xanh/Đỏ) hoặc I/O|Bật/Tắt nguồn cho bộ điều khiển logic (Màn hình, Bo mạch CNC).|
|**Machine Power**|Nút bấm (Xanh)|Đóng Contactor tổng, cấp nguồn động lực cho hệ thống Servo, Thủy lực và Trục chính.|
|**Emergency Stop (E-Stop)**|Nút nấm lớn (Đỏ, viền Vàng)|Cắt toàn bộ nguồn động lực và dừng khẩn cấp mọi chuyển động cơ học.|

**Phân tích kỹ thuật chuyên sâu:** Hệ thống khởi động của CNC-L200 được thiết kế theo cấu trúc hai lớp (Two-tier Power-up). Việc nhấn **NC Power ON** chỉ cung cấp điện áp điều khiển 24VDC để khởi động hệ điều hành CNC, nạp các tham số máy (Machine Parameters) và kiểm tra tín hiệu cảm biến. Máy hoàn toàn không có khả năng chuyển động ở trạng thái này. Chỉ khi nhấn **Machine Power**, hệ thống mới kích hoạt rơ-le an toàn, đóng điện áp cao (380V/415V) vào biến tần trục chính và các bộ khuếch đại Servo (Servo Amplifiers), đồng thời kích hoạt trạm bơm thủy lực.

**Nút Dừng khẩn cấp (E-Stop):** Về mặt cơ điện tử, E-Stop không gửi tín hiệu mềm qua phần mềm mà tạo ra một ngắt phần cứng (Hardware Interrupt) trực tiếp. Khi bị tác động, nó lập tức ngắt cuộn dây của contactor chính. Ngay lúc này, các biến tần sẽ chuyển năng lượng quán tính từ trục chính và các trục X/Z đang di chuyển tốc độ cao vào các điện trở xả (Brake Resistors) để thực hiện phanh động năng (Dynamic Braking) trong chưa tới 1 giây, đồng thời hệ thống phanh từ (Magnetic Brake) trên động cơ trục X sẽ đóng sập lại để chống rớt đài dao.

> ⚠️ \*\*NHẮC LẠI CẢNH BÁO TỪ CHƯƠNG 1:\*\* Nút E-Stop tuyệt đối \*\*không được dùng để thay thế quy trình LOTO\*\*. E-Stop chỉ đóng băng hệ thống tạm thời và dòng điện áp cao, áp suất thủy lực bẫy vẫn còn tồn tại ngầm bên trong máy. Lạm dụng E-Stop để tắt máy bảo dưỡng là vi phạm an toàn nghiêm trọng.

### 3.1.2. Cụm Chế độ hoạt động (Operation Modes)

|**Chế độ (Mode)**|**Biểu tượng/Ký hiệu**|**Ý nghĩa thực thi**|
|-|-|-|
|**AUTO (MEM)**|Hình trang giấy có mũi tên|Chạy tự động liên tục chương trình đã lưu trong bộ nhớ.|
|**EDIT**|Hình bút chì / Bàn phím|Chỉnh sửa, tạo mới hoặc truyền xuất chương trình CNC.|
|**MDI**|Hình ngón tay chỉ vào màn hình|Nhập dữ liệu thủ công (Manual Data Input) - Thực thi lệnh đơn lẻ.|
|**JOG / HANDLE**|Hình trục / Bánh xe tay quay|Chạy các trục thủ công liên tục (JOG) hoặc chạy vi bước bằng tay quay (MPG/HANDLE).|
|**COOLANT**|Hình vòi xịt nước (ON/OFF/AUTO)|Điều khiển thủ công cụm bơm dung dịch làm mát.|

**Phân tích kỹ thuật chuyên sâu:** Việc chuyển đổi giữa các chế độ (Modes) thực chất là thao tác thay đổi luồng dữ liệu (Data flow) đi vào bộ vi xử lý quỹ đạo của máy.

* Ở chế độ **EDIT**, bộ điều khiển đóng vai trò như một trình soạn thảo văn bản, khóa hoàn toàn các ngõ ra điều khiển chuyển động.
* Chế độ **AUTO** giải phóng quyền kiểm soát cho bộ nhớ (Memory), nơi máy tự động nội suy hàng ngàn dòng lệnh G-Code với tốc độ đọc trước (Look-ahead) cực nhanh để tạo ra biên dạng phức tạp.
* **JOG và HANDLE** trao quyền kiểm soát vật lý lại cho người vận hành. Chế độ HANDLE sử dụng một bộ phát xung thủ công (MPG). Khi vặn 1 nấc trên núm MPG, Encoder sẽ gửi số lượng xung tương ứng về bộ điều khiển, di chuyển trục X/Z ở các vạch chia vi mô (0.001mm, 0.01mm, 0.1mm), cực kỳ quan trọng để rà gá phôi và đo dao an toàn.
* **Chế độ MDI (Manual Data Input):** Đây là buồng đệm lệnh tạm thời. Lệnh gõ vào đây sẽ bị xóa sau khi thực thi. MDI được kỹ thuật viên sử dụng để gọi dao, thiết lập gốc tọa độ, hoặc kích hoạt/tắt các cơ cấu phụ trợ. Như đã quy định chặt chẽ ở Chương 1 (Bước 2 của quy trình chuẩn bị LOTO), người vận hành bắt buộc phải sử dụng bảng MDI để gõ lệnh `M05` (Dừng trục chính) và `M09` (Tắt hệ thống dung dịch làm mát) hoặc sử dụng nút **COOLANT OFF** vật lý trên HMI để đưa máy về trạng thái tĩnh trước khi tiến hành ngắt điện.

### 3.1.3. Cụm Thực thi \& Chiết áp (Execution \& Overrides)

|**Nút / Núm vặn**|**Ký hiệu / Dải số**|**Chức năng**|
|-|-|-|
|**Cycle Start**|Nút Xanh (Hình thoi/Mũi tên)|Kích hoạt bắt đầu chạy chương trình (AUTO) hoặc lệnh (MDI).|
|**Feed Hold**|Nút Đỏ (Hình bát giác)|Tạm dừng chạy dao (Trục X, Z dừng lại, Trục chính vẫn quay).|
|**Spindle Override**|Núm vặn (50% - 120%)|Điều chỉnh tỷ lệ phần trăm tốc độ trục chính so với lệnh S trong chương trình.|
|**Feedrate Override**|Núm vặn (0% - 150%)|Điều chỉnh tỷ lệ phần trăm tốc độ chạy dao so với lệnh F trong chương trình.|

**Phân tích kỹ thuật chuyên sâu:** **Cycle Start** và **Feed Hold** là bộ đôi nút bấm được sử dụng nhiều nhất. Điểm khác biệt sống còn về an toàn cần ghi nhớ: khi nhấn *Feed Hold*, bộ điều khiển chỉ cắt xung cấp cho động cơ Servo trục X và Z (dừng bước tiến dao), nhưng **động cơ trục chính vẫn tiếp tục quay** với tốc độ và mô-men xoắn định mức. Điều này giúp dao không bị kẹt hay gãy do phôi đứng lại đột ngột, nhưng người vận hành tuyệt đối không được mở cửa để thò tay vào buồng máy khi máy đang ở trạng thái Feed Hold.

Các núm vặn **Override (Chiết áp)** cho phép người vận hành can thiệp động (Dynamic bypass) vào thông số lập trình gốc để tinh chỉnh quá trình cắt gọt (khắc phục tiếng rít, tối ưu hóa quá trình bẻ phoi). **Feedrate Override** có thể ép máy chạy chậm lại (tiến về 0%) khi dao sắp chạm phôi để thử nghiệm an toàn (Dry run).

Đặc biệt đối với **Spindle Override**, sự can thiệp này tác động trực tiếp đến biến tần trục chính. Lệnh gốc được lập trình có thể là `S3300` (3300 Vòng/phút), nhưng nếu người vận hành vặn núm lên mức 120%, tốc độ trục chính sẽ bị ép tăng lên. Nhằm bảo vệ an toàn tối đa cho hệ thống (đặc biệt là tránh vượt quá ngưỡng lực ly tâm của mâm cặp), **phần mềm CNC đã thiết lập tham số giới hạn (Clamp Parameter)**. Cho dù người vận hành lập trình lệnh `S4000` và vặn núm chiết áp lên 120%, bộ điều khiển vẫn sẽ tự động cắt gọt (Clamp) và **khóa tốc độ thực tế ở mức trần 4000 RPM**, đảm bảo máy không bao giờ vượt qua giới hạn vòng quay thiết kế đã được nêu trong Chương 2.

> ⚠️ \*\*CẢNH BÁO ĐỘNG LỰC HỌC TỪ CHƯƠNG 2:\*\* Ngay cả khi tốc độ đã được khóa trần ở 4000 RPM, kỹ thuật viên vẫn phải cẩn trọng tột độ. Dưới tác động của tốc độ cắt cực đại này, khối lượng của mâm cặp thủy lực 8 inch kết hợp cùng phôi sẽ tạo ra lực ly tâm khổng lồ, làm giảm nghiêm trọng lực kẹp tĩnh ban đầu của các ngàm (Jaws). Việc tăng tốc độ vô tội vạ mà không tính toán đến độ suy giảm lực kẹp sẽ dẫn đến hiện tượng trượt phôi hoặc vỡ ngàm, gây văng phôi tốc độ cao phá nát buồng máy và gây nguy hiểm chết người.

## 3.2. Cơ chế hoạt động các cụm cơ khí cốt lõi

Việc nắm vững nguyên lý động lực học và kết cấu cơ khí bên trong máy CNC-L200 là điều kiện tiên quyết để vận hành thiết bị ở hiệu suất tối đa mà không vượt quá các giới hạn rạn nứt cơ học hoặc gây mất an toàn. Dưới đây là sự mổ xẻ chi tiết vào các thành phần mang tính nền tảng nhất.

### 3.2.1. Cụm Mâm cặp thủy lực (Hydraulic Chuck \& Rotary Cylinder)

Mâm cặp thủy lực 8 inch trên CNC-L200 không phải là một cơ cấu kẹp đơn giản, mà là điểm cuối của một chuỗi truyền lực cơ - thủy lực phức tạp đòi hỏi độ chính xác tuyệt đối. Hệ thống này được điều khiển vật lý thông qua **Cụm Bàn đạp chân (Foot Switch)** đặt phía trước máy, cho phép người vận hành sử dụng chân để đóng/mở ngàm kẹp, giải phóng hai tay để nâng đỡ vật liệu nặng.

**Chuỗi truyền lực và Cơ chế hoạt động:**
Năng lượng kẹp bắt nguồn từ **Trạm nguồn thủy lực (HPU)** cung cấp dải áp suất liên tục từ $3.5 - 6.0 \\text{ MPa}$. Áp suất này được dẫn vào **Xylanh thủy lực xoay (Rotary Cylinder)** được lắp đặt ngay tại đuôi trục chính. Điểm đặc biệt của xylanh này là vỏ ngoài đứng yên trong khi trục piston bên trong có thể quay cùng tốc độ với trục chính.
Khi người vận hành tác động vào bàn đạp chân, van điện từ đảo chiều dòng áp suất vào buồng kẹp, piston lùi lại, kéo theo một **Ống kéo (Drawtube)** bằng thép cường lực chạy xuyên dọc qua tâm lỗ trục chính. Ở đầu kia, ống kéo kết nối trực tiếp với **Cơ cấu chêm trượt (Wedge Plunger)** nằm sâu bên trong mâm cặp. Cơ cấu Wedge hoạt động như một mặt phẳng nghiêng, làm nhiệm vụ chuyển đổi chuyển động kéo tịnh tiến (tuyến tính) của ống kéo thành chuyển động hướng tâm (xuyên tâm), mạnh mẽ đẩy các **Ngàm kẹp (Jaws/Master Jaws)** cắn chặt vào phôi liệu.

**Phân tích hiện tượng suy giảm lực kẹp động (Dynamic Grip Loss):**
Khi máy ở trạng thái tĩnh (0 RPM), ngàm kẹp ép vào phôi với 100% lực kẹp thủy lực (phụ thuộc vào mức áp suất $3.5 - 6.0 \\text{ MPa}$ đã thiết lập). Tuy nhiên, nguyên lý động lực học thay đổi hoàn toàn khi trục chính bắt đầu gia tốc.
Mỗi cụm ngàm kẹp là một khối lượng kim loại đáng kể. Khi xoay, chúng tuân theo định luật vật lý về **Lực ly tâm (**$F = m \\cdot \\omega^2 \\cdot r$**)**. Lực ly tâm này có hướng văng ra xa tâm trục, nghĩa là nó **ngược chiều trực tiếp** với lực ép của ngàm đang cố cắn vào phôi. Khi trục chính tiệm cận tốc độ cực đại **4000 RPM**, lực ly tâm tăng theo hàm bình phương của vận tốc góc ($\\omega^2$). Lúc này, lực ly tâm sẽ thắng một phần lớn lực kéo của cơ cấu Wedge Plunger, khiến lực kẹp thực tế (Dynamic Grip) sụt giảm một cách nguy hiểm so với lực tĩnh ban đầu.

Chính vì lý do này, kỹ thuật viên bắt buộc phải tuân thủ nghiêm ngặt **giới hạn trọng lượng phôi đã quy định tại Chương 2 (150 kg khi chỉ kẹp mâm cặp và 300 kg khi có hỗ trợ chống tâm ụ động)**. Nếu bỏ qua các giới hạn này khi chạy ở tốc độ cao, phôi sẽ lỏng ra ngay giữa quá trình tiện tinh.

> ⚠️ \*\*CẢNH BÁO AN TOÀN BẢO DƯỠNG MÂM CẶP:\*\* Nhắc lại từ Bước 5 - Quy trình LOTO ở Chương 1. Sự kết hợp giữa áp suất thủy lực lớn và cơ cấu Wedge Plunger tạo ra một cái bẫy cơ học giấu kín. Kỹ thuật viên tuyệt đối cấm tháo các ốc vít lục giác giữ ngàm kẹp khi chưa xả hết áp suất nhánh thủy lực tại van điện từ (đưa đồng hồ về 0 MPa). Nếu cố tình nới ốc khi ống kéo vẫn đang căng dưới áp lực, ngàm kẹp sẽ biến thành một viên đạn, phóng văng ra ngoài hoặc kẹp sập lại một cách mất kiểm soát, gây nát tay hoặc tổn thương nghiêm trọng.

### 3.2.2. Khung Băng máy nghiêng 45 độ (45-Degree Slant Bed Structure)

Nền tảng của sự chính xác trên máy CNC-L200 nằm ở phần khung bệ. Máy không sử dụng thép hàn ghép mà được đúc nguyên khối từ **Gang Meehanite** (một loại gang xám tinh luyện chứa các tinh thể graphite vảy phân bố đều) với tổng trọng lượng khổng lồ lên tới **4200 kg**.

Để chống lại lực vặn xoắn (Torsion) sinh ra bởi mô-men xoắn 167 N.m của trục chính, bên trong lòng khối gang được đúc tích hợp mạng lưới **gân gia cường chữ X (X-ribs)**. Cấu trúc mạng gân này giúp hấp thụ và dập tắt các sóng rung động biên độ cao trước khi chúng kịp truyền đến các ray dẫn hướng.

Việc thiết kế góc nghiêng **45 độ** cho băng máy không phải là yếu tố thẩm mỹ, mà mang lại hai lợi ích kỹ thuật mang tính sống còn:

* **Động lực học phoi cắt (Chip Flow) và Ổn định nhiệt:** Trong nguyên công tiện phá thô vật liệu cứng, nhiệt độ tại vùng cắt có thể lên tới $800^\\circ \\text{C}$. Nếu sử dụng băng máy phẳng, phoi nóng đỏ sẽ tích tụ trên thanh ray, làm gang giãn nở nhiệt cục bộ và phá vỡ dung sai hình học. Với độ dốc 45 độ, trọng lực buộc dòng phoi cắt và dung dịch làm mát tự động trượt thẳng xuống máng xả của băng tải bên dưới ngay khi vừa đứt lìa. Khung máy hoàn toàn không bị hấp thụ nhiệt lượng từ phoi thải.
* **Công thái học và An toàn cuốn ép (Ergonomics \& Entanglement Safety):** Đối với các máy băng phẳng hoặc nghiêng góc nhỏ, tâm trục chính nằm ở vị trí khá xa phía trong, buộc kỹ thuật viên phải nhoài người qua rào chắn (Reach-in) mỗi khi gá lắp phôi nặng hoặc dùng đồng hồ so rà mâm cặp. Góc nghiêng 45 độ đưa trục chính và mâm cặp tiến sát hơn về phía trước cửa máy. Thợ vận hành có thể thao tác ở tư thế đứng thẳng, gần với máy hơn. Điều này trực tiếp làm giảm nguy cơ quần áo bị vướng hay tay bị cuốn ép (Entanglement Hazard) vào các bộ phận quay (như cảnh báo dán trên cửa máy ở Chương 1), đồng thời giảm thiểu tổn thương cột sống do phải bưng bê phôi ở tư thế sai công thái học.

### 3.2.3. Cụm Đài dao Servo tốc độ cao (High-Speed Servo Turret)

Đài dao 12 vị trí trên CNC-L200 hoạt động liên tục trong một môi trường làm việc cực kỳ khắc nghiệt. Trục X di chuyển với tốc độ tối đa lên đến $24 \\text{ m/phút}$, trong khi trục Z đạt mức $30 \\text{ m/phút}$. Ở những mức gia tốc lớn này, sự ổn định và tốc độ thay dao quyết định trực tiếp đến năng suất tổng thể.

**Cơ chế phân độ và Chu trình chuyển dao 0.2 giây:**
Sức mạnh cốt lõi của hệ thống này nằm ở sự kết hợp hoàn hảo giữa Động cơ AC Servo (đảm nhận việc quay định vị chính xác) và hệ thống Thủy lực (đảm nhận việc khóa cứng cơ khí). Toàn bộ chu trình thay dao diễn ra chỉ trong **0.2 giây** thông qua một trình tự 3 bước (Sequence) tính toán bằng phần nghìn giây:

1. **Thủy lực xả áp nhả khớp (Unclamp):** Ngay khi vi xử lý nhận lệnh gọi dao (ví dụ `T0101`), van điện từ cấp áp suất ngược đẩy mâm dao (Turret disk) trượt nhẹ ra ngoài khoảng $5 \\text{ mm}$ dọc theo trục tâm, tách rời sự liên kết của các bánh răng khóa.
2. **Động cơ Servo phân độ (Index):** Ngay khoảnh khắc các răng vừa tách rời, động cơ Servo với mô-men xoắn cao xoay mâm dao đến đúng trạm mục tiêu với gia tốc cực lớn và phanh lại bằng Encoder tuyệt đối.
3. **Thủy lực khóa khớp nối răng (Clamp):** Áp suất thủy lực lập tức đổi chiều, kéo mâm dao thụt lùi vào trong, ép chặt **Khớp nối răng 3 mảnh (Curvic Coupling)**.

**Sức mạnh của Khớp nối răng Curvic Coupling:**
Tại sao đài dao không dùng chốt cơ khí mà phải dùng Curvic Coupling? Khớp Curvic bao gồm các vòng răng dạng lồi/lõm (convex/concave) xen kẽ nhau. Khi lực ép thủy lực khổng lồ đẩy hai nửa khớp gài lại, các bề mặt răng xéo sẽ tự trượt vào nhau tạo thành hiệu ứng tự định tâm (Self-centering) tuyệt đối. Cấu trúc này mở rộng tối đa diện tích tiếp xúc kim loại, cho phép cụm đài dao hấp thụ triệt để lực va đập dội ngược (Impact load) khi phay/tiện không liên tục, đồng thời duy trì độ lặp lại vị trí siêu hạng ở mức $\\pm 0.002 \\text{ mm}$.

> ⚠️ \*\*CẢNH BÁO AN TOÀN CƠ HỌC TỪ CHƯƠNG 1:\*\* Khối lượng của mâm đài dao cộng với 12 cán dao là rất nặng. Thông thường, đài dao ở trạng thái không cân bằng tĩnh (ví dụ: gắn nhiều cán dao thép phay lớn ở một bên). Nếu trong quá trình máy đang chạy hoặc đang thay dao mà \*\*đột ngột mất điện\*\* hoặc \*\*mất áp suất thủy lực\*\*, cơ cấu Curvic Coupling sẽ bị nhả ra (Unclamp) trong khi phanh từ (Motor Brake) chưa kịp đóng. Trọng lực lập tức sẽ kéo phần nặng nhất của mâm dao rơi tự do (Free-fall / Drop) theo chiều quay. Nghiêm cấm đưa tay hoặc chui đầu vào khu vực đài dao để thao tác gá dao nếu máy chưa được khóa LOTO hoàn toàn, nguy cơ mâm dao rơi đập dập nát bàn tay là rất cao.

### 3.2.4. Cụm Ụ động và Nòng thủy lực (Tailstock \& Hydraulic Quill)

Để hỗ trợ nguyên công tiện các trục dài (tỉ lệ L/D lớn), cụm Ụ động trên CNC-L200 được thiết kế chia làm hai phần độc lập: **Thân ụ động (Tailstock Body)** cứng vững được kéo di chuyển và khóa chặt trực tiếp xuống băng máy (thông qua chốt cơ khí hoặc hàm kẹp thủy lực), và một **Nòng ụ động (Hydraulic Quill)** đường kính $65 \\text{ mm}$ mang mũi chống tâm chuẩn MT4 có thể thò/thụt độc lập với hành trình tối đa $80 \\text{ mm}$. Tương tự mâm cặp, nòng ụ động cũng được điều khiển sự thò/thụt thông qua cụm **Bàn đạp chân (Foot Switch)** kép (pedal thứ hai) đặt dưới sàn máy.

**Khả năng "Chống tâm bù nhiệt" (Thermal Compensation Capability):**
Sự ưu việt của nòng ụ động điều khiển bằng áp suất thủy lực ($3.5 - 6.0 \\text{ MPa}$) so với nòng quay tay (Manual quill) nằm ở khả năng bù trừ biến dạng nhiệt hoàn toàn tự động.
Trong quá trình tiện phá thô tốc độ cao, phôi thép dài hấp thụ năng lượng cắt và nóng lên dữ dội, dẫn đến hiện tượng **giãn nở tuyến tính (Linear Thermal Expansion)** dọc theo trục Z.

* Nếu dùng nòng ụ động cố định (cơ khí), phôi giãn nở sẽ tạo ra một lực đẩy dọc trục khổng lồ (Axial thrust) ép ngược lại mũi tâm, chắc chắn sẽ làm nổ vỡ các ổ bi tiếp xúc góc (Angular contact bearings) bên trong mũi tâm quay (Live Center), hoặc làm cong võng phôi liệu.
* Tuy nhiên, nòng thủy lực hoạt động như một lò xo hằng số. Khi phôi giãn nở và đẩy lại, áp suất bên trong xylanh nòng ụ động sẽ giữ nguyên (do van xả áp điều tiết). Nòng Quill tự động lùi lại ở khoảng cách siêu vi mô (micro-millimeters) để triệt tiêu ứng suất, duy trì một lực đẩy hằng số liên tục (từ $2.5 - 4.5 \\text{ kN}$) ôm sát vào lỗ tâm phôi. Điều này giúp mũi tâm không bao giờ bị quá tải và phôi luôn thẳng tuyệt đối.

> ⚠️ \*\*CẢNH BÁO "BẪY ÁP SUẤT" (TRAPPED PRESSURE) TRONG BẢO DƯỠNG:\*\* Như đã quy định rất rõ trong Bước 5 (LOTO - Chương 1) và phần thông số ụ động (Chương 2), xylanh nòng ụ động được trang bị các \*\*Van một chiều chống lún (Pilot-operated check valves)\*\*. Nhiệm vụ của van này là giữ nguyên áp lực không cho nòng ụ động thụt lùi làm rớt phôi nếu nhà máy bị cúp điện đột ngột.
> Hệ lụy của tính năng an toàn này là: Ngay cả khi đã tắt cầu dao tổng và máy hoàn toàn chết, \*\*áp suất thủy lực cao (có thể lên tới 6.0 MPa) vẫn bị giam lỏng (Trapped pressure)\*\* giữa cụm van và xylanh nòng. Nếu kỹ thuật viên tháo dỡ các cút nối hoặc rã nòng ụ động mà chưa thực hiện xả áp bằng van xả thủ công (Manual Override), áp suất này sẽ đột ngột giải phóng. Nòng nén hoặc các linh kiện thủy lực sẽ lao ra phía trước với lực ép tĩnh vài tấn, dư sức đâm xuyên hoặc cắt đứt chi thể.

# Chương 4: Hướng dẫn vận hành cơ bản

### 4.1. Quy trình Khởi động (Power ON) và Tắt máy chuẩn (Power OFF)

**Quy trình Khởi động máy (Power ON):**
Để đảm bảo an toàn cho hệ thống điện, cơ khí và thủy lực, quá trình khởi động phải tuân thủ nghiêm ngặt các bước sau:

1. **Kiểm tra môi chất:** Kiểm tra cảm quan mức dầu bôi trơn ray trượt/vít me, mức dầu thủy lực tại trạm HPU (đảm bảo đủ trong thùng 40 Lít) và mức dung dịch làm mát (trong thùng 120 Lít).
2. **Kiểm tra áp suất:** Đảm bảo áp suất khí nén đạt tiêu chuẩn ($0.6 - 0.8 \\text{ MPa}$) và áp suất dầu thủy lực đạt ngưỡng ($3.5 - 6.0 \\text{ MPa}$).
3. **Cấp nguồn tổng:** Đóng cầu dao tổng (Main Breaker) nằm ở phía sau máy.
4. **Khởi động NC:** Nhấn nút **NC Power ON** trên bảng điều khiển và chờ hệ điều hành tải hoàn tất.
5. **Mở khóa an toàn:** Nhả nút Dừng khẩn cấp (**E-Stop**) bằng cách xoay núm theo chiều mũi tên.
6. **Cấp điện áp cao:** Nhấn nút **Machine Power** (hoặc Machine Ready) để cấp nguồn điện áp cao cho hệ thống Servo, biến tần trục chính và Bơm thủy lực.

**Quy trình Tắt máy chuẩn (Power OFF):**

> \*\*Lưu ý:\*\* Đây là quy trình tắt máy cơ bản sau khi kết thúc ca làm việc, tuyệt đối không thay thế cho quy trình LOTO (Lockout/Tagout) khi cần bảo dưỡng hoặc sửa chữa sâu.

1. **Di chuyển trục an toàn:** Sử dụng tay quay (HANDLE) hoặc chạy JOG để đưa trục X và trục Z ra xa khỏi ụ động và mâm cặp để tạo không gian an toàn.
2. **Dừng các hệ thống phụ:** Chuyển sang chế độ **MDI**, gõ và thực thi lệnh **M05** (Dừng trục chính) và **M09** (Tắt dung dịch làm mát).
3. **Tắt NC:** Nhấn nút **NC Power OFF** để tắt hệ điều hành màn hình và ngắt tín hiệu điều khiển.
4. **Ngắt nguồn tổng:** Tắt cầu dao tổng ở phía sau tủ điện máy.

\---

### 4.2. Cách đưa máy về điểm gốc (Zero Return / Reference Point)

**Mục đích:**
Sau khi bật máy, việc đưa máy về điểm gốc (Zero Return) là bắt buộc để các Encoder tuyệt đối đồng bộ lại tọa độ thực tế của cụm cơ khí với tọa độ hiển thị trên phần mềm điều khiển.

> ⚠️ \*\*CẢNH BÁO CỰC KỲ QUAN TRỌNG (CRASH HAZARD):\*\*
> Trước khi thực hiện lệnh tự động về gốc, luôn dùng chế độ \*\*JOG\*\* đưa \*\*trục X lùi về hướng dương (+)\*\* để đài dao được nâng lên cao, tránh nguy cơ va chạm (Crash) thảm khốc vào ụ động hoặc mâm cặp. Chỉ sau khi trục X đã ở vị trí an toàn, mới tiếp tục đưa \*\*trục Z lùi về hướng dương (+)\*\*.

**Quy trình thực hiện:**

1. Đảm bảo các trục đã được di chuyển ra xa khu vực mâm cặp/ụ động (như cảnh báo trên).
2. Xoay núm chọn chế độ (Mode Select) sang vị trí **REF** (hoặc **HOME / ZERO RETURN**).
3. Nhấn và giữ (hoặc nhấn 1 lần tùy đời máy) nút hướng **+X** trên bảng điều khiển. Trục X sẽ tự động chạy về điểm gốc. Chờ đến khi đèn báo **X Zero** sáng lên.
4. Tiếp tục nhấn nút hướng **+Z**. Trục Z sẽ tự động chạy về điểm gốc. Chờ đến khi đèn báo **Z Zero** sáng lên. Khâu đồng bộ hoàn tất.

\---

### 4.3. Quy trình Gá lắp phôi (Workpiece Clamping)

Quy trình gá phôi yêu cầu sự chính xác để duy trì độ đồng tâm và đảm bảo an toàn động lực học khi cụm mâm cặp thủy lực 8 inch vận hành ở tốc độ cao. Các bước thực hiện tuần tự:

1. **Làm sạch ngàm kẹp:** Sử dụng súng xịt khí nén làm sạch toàn bộ phoi cắt và dung dịch làm mát bám trên bề mặt các ngàm kẹp (Jaws).

   * *Lý do:* Loại bỏ vật cản giúp đảm bảo bề mặt tiếp xúc hoàn hảo giữa ngàm và phôi, tránh hiện tượng gá kẹp bị lệch tâm hoặc suy giảm lực ma sát.
2. **Chuyển chế độ an toàn:** Trên bảng điều khiển HMI, chuyển máy sang chế độ **HANDLE** hoặc **JOG**.

   * *Lý do:* Khóa các luồng lệnh tự động, loại trừ hoàn toàn rủi ro trục chính hoặc các trục X/Z tự động di chuyển gây tai nạn trong lúc tay đang thao tác trong buồng máy.
3. **Đưa phôi vào mâm cặp:** Nâng phôi và đưa vào giữa vị trí các ngàm kẹp, tận dụng thiết kế băng máy góc nghiêng 45 độ để tựa đỡ phôi.

   * *Lý do:* Khung băng máy nghiêng 45 độ mang lại lợi thế công thái học vượt trội, đưa trục chính tiến sát về phía người vận hành, giảm thiểu chấn thương cột sống khi bưng bê phôi nặng và hạn chế rủi ro phải nhoài người vào sâu trong máy.
4. **Kích hoạt kẹp phôi:** Giữ phôi bằng tay, sau đó đạp Bàn đạp chân (Foot Switch) thứ nhất để xylanh thủy lực kéo ống Drawtube, ép chặt ngàm kẹp lại.

   * *Lý do:* Cơ chế bàn đạp chân giúp giải phóng hai tay người thợ, cho phép kiểm soát hoàn toàn tư thế của phôi liệu cho đến khi mâm cặp thiết lập đủ lực kẹp thủy lực tĩnh.

> 🛑 \*\*CẢNH BÁO AN TOÀN ĐỘNG LỰC HỌC:\*\*
> \* \*\*Tuân thủ quy tắc L/D:\*\* Nếu tỷ lệ L/D (Chiều dài phần phôi nhô ra / Đường kính phôi) lớn hơn 3, BẮT BUỘC phải chuyển sang Mục 4.4 để thiết lập ụ động chống tâm nhằm tránh võng phôi.
> \* \*\*Giới hạn trọng lượng tĩnh và động:\*\* Trọng lượng phôi gá kẹp lơ lửng (chỉ dùng mâm cặp) tuyệt đối không được vượt quá $150 \\text{ kg}$. Nếu vượt quá, khi máy tăng tốc lên 4000 RPM, lực ly tâm sẽ thắng lực ép thủy lực của cơ cấu Wedge Plunger, gây văng phôi đạn đạo.
> \* \*\*Cấm sử dụng găng tay sợi:\*\* Tuyệt đối không đeo găng tay sợi/vải khi thao tác gá phôi để tránh rủi ro cuốn ép cơ học.

\---

### 4.4. Quy trình Vận hành Ụ động (Tailstock \& Quill Operation)

Khi gia công các chi tiết trục dài, việc sử dụng ụ động là bắt buộc. Hệ thống chống tâm bù nhiệt của CNC-L200 được thao tác như sau:

1. **Điều chỉnh áp suất chống tâm:** Dựa trên vật liệu và độ lớn của phôi, điều chỉnh van áp suất thủy lực dành riêng cho ụ động (thường nằm gần HPU hoặc đuôi máy) về mức tiêu chuẩn **3.5 - 6.0 MPa**. Áp suất này sẽ tạo ra lực đẩy từ **2.5 đến 4.5 kN** duy trì hằng số liên tục để bù trừ biến dạng nhiệt của phôi.
2. **Định vị thân ụ động:** Mở khóa (Unclamp) thân ụ động. Kéo thân ụ động dọc theo băng máy (thủ công hoặc dùng chốt kéo kết nối với cụm trục Z) đến vị trí sao cho khoảng cách từ mũi tâm (Live Center) đến mặt đầu phôi còn khoảng $30 - 50 \\text{ mm}$. Khóa chặt (Clamp) thân ụ động xuống băng máy.
3. **Kích hoạt nòng ụ động (Quill):** Đạp **Bàn đạp chân thứ hai** (Foot Switch cụm Tailstock). Nòng thủy lực (Quill) sẽ vươn ra (tối đa $80 \\text{ mm}$) và ép chặt mũi tâm chuẩn MT4 vào lỗ tâm của phôi liệu. Đảm bảo đồng hồ áp suất đạt ngưỡng đã thiết lập trước khi gia công.

> ⚠️ \*\*CẢNH BÁO AN TOÀN - BẪY ÁP SUẤT:\*\* Nhắc lại từ Chương 1 và 3, van chống lún sẽ giam lỏng áp suất bên trong nòng xylanh ngay cả khi tắt máy. Tuyệt đối không tháo dỡ cút nối thủy lực hoặc rã nòng ụ động nếu chưa dùng van cơ khí dự phòng xả hết "áp suất bẫy" này về 0 MPa.

\---

### 4.5. Quy trình Gá dao lên đài dao (Tool Mounting)

Đài dao Servo 12 vị trí sử dụng cơ cấu khóa khớp răng Curvic Coupling yêu cầu quy trình tháo lắp chặt chẽ để không phá vỡ độ chính xác lặp lại của dao cụ.

1. **Chuyển chế độ vận hành:** Chuyển hệ thống sang chế độ **JOG** hoặc **HANDLE**.
2. **Định vị trạm dao (Index):** Sử dụng nút gọi dao trên bảng điều khiển để xoay đài dao đưa vị trí trạm trống cần lắp ra góc thao tác thuận lợi nhất.
3. **Vệ sinh vị trí gá:** Lau sạch và dùng khí nén xịt kỹ bề mặt rãnh gá dao vuông ($25 \\times 25 \\text{ mm}$) hoặc lỗ gá cán tròn ($\\varnothing 40 \\text{ mm}$). Bất kỳ hạt phoi nào kẹt lại cũng làm lệch tâm và giảm độ cứng vững của dao.
4. **Lắp và siết lực:** Lắp cán dao vào rãnh, dùng cờ lê lực (Torque wrench) siết đều các bulong theo đúng thông số. Siết thiếu lực khiến dao bị tuột; siết quá lực gây cháy ren lục giác.

> 🛑 \*\*CẢNH BÁO AN TOÀN THAO TÁC:\*\*
> \* \*\*Nguy cơ kẹp dập (Pinch Point):\*\* Chu trình tháo khớp (Unclamp) và xoay phân độ của đài dao Servo diễn ra chớp nhoáng trong \*\*$0.2$ giây\*\*. Luôn rút tay hoàn toàn khỏi không gian ụ dao trước khi nhấn nút Index trên HMI để tránh dập nát ngón tay.
> \* Đảm bảo chíp dao (Insert) được lắp đúng hướng tương thích với chiều quay lập trình của trục chính (M03 hoặc M04).

\---

### 4.6. Quy trình Đo bù dao thủ công (Manual Tool Offset)

Mỗi dụng cụ cắt đều có kích thước khác nhau. Đo bù dao (Tool Offset) là thao tác "dạy" cho bộ điều khiển biết chính xác khoảng cách từ mũi dao hiện tại đến tâm trục chính (Trục X) và vị trí mặt đầu của phôi (Trục Z), cũng như khai báo hình học mũi dao phục vụ cho bù trừ bán kính dao tự động.

**Quy trình Đo bù dao Trục Z (Z-Axis Offset):**

1. Chuyển hệ thống sang chế độ **HANDLE** (Sử dụng tay quay MPG).
2. Khởi động trục chính quay ở tốc độ chậm (MDI -> `M03 S...`).
3. Sử dụng tay quay MPG, nhích dao đến khi mũi dao chạm nhẹ và cắt một lớp rất mỏng trên mặt đầu của phôi (Face cut).
4. Giữ nguyên vị trí trục Z (không lùi dao), vào bảng **Offset / Geometry** trên màn hình HMI, di chuyển con trỏ đến số thứ tự dao tương ứng, gõ **Z0** và nhấn **Measure / Input**.

**Quy trình Đo bù dao Trục X (X-Axis Offset):**

1. Vẫn ở chế độ **HANDLE**, từ từ quay MPG cho dao ăn vào phôi và tiện một đoạn nhỏ dọc theo đường kính ngoài của phôi (O.D. cut).
2. **CHỈ LÙI DAO RA THEO HƯỚNG TRỤC Z** (kéo dao ra khỏi mặt đầu phôi). **Tuyệt đối không di chuyển trục X** để bảo toàn vị trí đo.
3. Dừng trục chính (M05). Dùng thước Panme (Micrometer) đo chính xác đường kính đoạn phôi vừa tiện.
4. Vào bảng **Offset / Geometry**, tại dòng dao tương ứng, gõ **X\[giá trị đường kính vừa đo]** (ví dụ: `X45.230`) và nhấn **Measure / Input**.

**Khai báo Tham số Hình học mũi dao (Tool Nose Radius \& Orientation):**
Để bộ điều khiển có thể chạy đúng các lệnh bù trừ bán kính dao (G41 / G42) khi phay vát (Chamfer) hoặc bo cung (Radius), bắt buộc phải khai báo 2 thông số sau trên cùng dòng dao vừa đo:

1. **Cột R (Radius):** Nhập bán kính góc bo của chíp dao (Ví dụ: `0.4` đối với chíp R0.4, hoặc `0.8` đối với chíp R0.8).
2. **Cột T (Tip / Orientation):** Nhập mã phương hướng của mũi dao so với tâm gia công (Từ 1 đến 9). Đối với dao tiện ngoài tiêu chuẩn (hướng dao từ dưới lên và cắt về mâm cặp), mã thường dùng là **3**.

> 🛑 \*\*CẢNH BÁO AN TOÀN KHI ĐO DAO (CRASH HAZARD):\*\*
> \* Khi mũi dao đã tiến sát vào phôi (khoảng cách $< 2 \\text{ mm}$), BẮT BUỘC phải chuyển tay quay MPG sang chế độ chia vi bước nhỏ nhất (\*\*$0.01 \\text{ mm}$ hoặc $0.001 \\text{ mm}$\*\*). Việc dùng bước tiến lớn ($1 \\text{ mm}$) sẽ dễ dẫn đến đâm sầm (Crash) mũi dao vào phôi hoặc mâm cặp, làm vỡ cụm vòng bi trục chính trị giá hàng ngàn USD.

# Chương 5: Bảo dưỡng định kỳ \& Xử lý sự cố (Troubleshooting)

Sự vận hành chính xác và bền bỉ của máy tiện CNC-L200 không chỉ đến từ thiết kế cơ khí ban đầu mà còn phụ thuộc hoàn toàn vào chế độ chăm sóc, bảo dưỡng kỷ luật của người sử dụng. Việc tuân thủ nghiêm ngặt lịch bảo dưỡng định kỳ chính là chìa khóa sống còn để duy trì độ chính xác của máy theo đúng chuẩn dung sai hình học và vị trí (ISO 230-1). Những can thiệp bảo dưỡng đúng lúc sẽ ngăn chặn sự suy thoái cơ học, bảo vệ nguyên vẹn cấu trúc chống vặn xoắn của băng máy đúc Meehanite, duy trì độ rơ bằng không (zero backlash) của cụm vít me bi cấp C3, và đảm bảo sự ổn định nhiệt cho hệ thống vòng bi trục chính tiếp xúc góc siêu chính xác cấp P4. Bỏ qua các bước bảo dưỡng hoặc thực hiện sai quy trình không chỉ dẫn đến hiện tượng sai lệch kích thước phôi (như lỗi vảy cá), mà còn mở đường cho các thảm họa va đập cơ học (Crash) tiêu tốn hàng ngàn USD để khắc phục.

> ⚠️ \*\*CẢNH BÁO AN TOÀN BẢO DƯỠNG (KẾ THỪA CHƯƠNG 1):\*\* Ngoại trừ các thao tác kiểm tra ngoại quan (nhìn qua mắt trâu) và đọc đồng hồ đo, \*\*BẮT BUỘC\*\* toàn bộ nhân viên kỹ thuật phải thực hiện đầy đủ \*\*Quy trình LOTO 5 Bước\*\* trước khi cầm cờ lê tháo lắp, vệ sinh sâu hoặc can thiệp vào bất kỳ cụm chi tiết nào. Xin nhắc lại: Nút dừng khẩn cấp (E-Stop) tuyệt đối KHÔNG ĐƯỢC sử dụng để thay thế cho quy trình cách ly năng lượng (LOTO). E-Stop vẫn giam lỏng điện áp cao trong biến tần và áp suất bẫy (Trapped pressure) bên trong các van một chiều.

## 5.1. Lịch bảo dưỡng định kỳ (Preventive Maintenance Schedule)

Lịch bảo dưỡng dưới đây được phân chia theo chu kỳ thời gian thực tế hoạt động của máy. Kỹ thuật viên bảo trì phải đánh dấu vào "Checklist" sau mỗi ca làm việc. Mọi chỉ số sai lệch phải được báo cáo ngay cho Kỹ sư trưởng.

### 5.1.1. Bảng bảo dưỡng Hàng ngày (Daily Maintenance)

Thực hiện vào đầu mỗi ca làm việc (trước khi khởi động trục chính) và cuối ca làm việc.

|Hạng mục|Vị trí kiểm tra|Thao tác kỹ thuật chi tiết|Chú ý an toàn \& Cảnh báo (Safety Notes)|
|-|-|-|-|
|**Hệ thống Thủy lực (HPU)**|Trạm nguồn HPU đặt phía sau máy.|Quan sát mắt trâu trên **thùng chứa 40 Lít**. Đảm bảo mức dầu luôn ở khoảng 80% - 90%. Kiểm tra đồng hồ áp suất tổng phải chỉ đúng dải **3.5 - 6.0 MPa** khi bơm chạy. Lắng nghe tiếng ồn của bơm màng (nếu có tiếng rít lạ là dấu hiệu e khí hoặc thiếu dầu).|Chỉ mở nắp châm thêm dầu khi máy đã tắt hoàn toàn. Tuyệt đối không để bụi bẩn hoặc phoi cắt rơi vào phễu rót, vì cặn bẩn sẽ làm kẹt các lõi van điện từ.|
|**Dung dịch làm mát (Coolant)**|Thùng chứa Coolant (Dung tích **120 Lít**) bên dưới băng tải phoi.|Kiểm tra mức dung dịch qua phao cơ. Đo nồng độ dung dịch bằng khúc xạ kế (Brix Refractometer) để duy trì tỷ lệ pha tiêu chuẩn (thường từ 6-10%). Bổ sung nước/dầu cắt gọt nếu hao hụt. Kiểm tra áp suất bơm tưới nguội đạt **0.3 - 0.5 MPa**.|**Cảnh báo trơn trượt:** Lau sạch ngay lập tức dầu/nước làm mát vương vãi trên sàn. Đeo găng tay nitrile khi pha dung dịch để tránh viêm da tiếp xúc.|
|**Hệ thống Khí nén**|Cụm FRL (Lọc - Điều áp - Bôi trơn) hông máy.|Kiểm tra đồng hồ áp kế chính, xác nhận nguồn khí từ xưởng cấp vào ổn định ở mức **0.6 - 0.8 MPa**. Kéo nhẹ van xả đáy tự động (Drain valve) dưới cốc lọc để đẩy toàn bộ nước ngưng tụ và nhũ tương dầu ra ngoài.|**Nguy cơ văng bắn:** Không ghé sát mặt vào cốc lọc khi kéo van xả áp. Hơi nước và cặn bẩn xịt ra với áp suất 0.8 MPa có thể gây tổn thương niêm mạc mắt.|
|**Vệ sinh Băng máy \& Cơ cấu trượt**|Băng máy nghiêng **45 độ**, Telescopic covers (tấm che ray trục X/Z).|Tận dụng độ dốc 45 độ, dùng chổi lông mềm hoặc thanh cào nhựa lùa toàn bộ phoi cắt và mạt kim loại rơi xuống máng xả băng tải. Lau sạch các mảng phoi dính trên mặt ngàm mâm cặp.|🛑 **CẤM KỴ:** Tuyệt đối **KHÔNG dùng súng xịt khí nén** xịt thẳng vào các khe hở của tấm che ray che vít me bi trục X/Z. Áp suất 0.8 MPa sẽ ép ngược mạt phoi siêu nhỏ và nước làm mát xuyên qua phớt chắn bụi, phá nát các viên bi bên trong vít me bi cấp C3.|

### 5.1.2. Bảng bảo dưỡng Hàng tuần (Weekly Maintenance)

Thực hiện vào ngày cuối cùng của tuần làm việc, yêu cầu dừng máy tối thiểu 30 phút.

|Hạng mục|Vị trí kiểm tra|Thao tác kỹ thuật chi tiết|Chú ý an toàn \& Cảnh báo (Safety Notes)|
|-|-|-|-|
|**Lưới lọc Coolant**|Bơm làm mát (cắm trong thùng 120 Lít).|Rút cụm bơm tưới nguội lên, tháo lưới lọc hút (Suction filter) ở đáy bơm. Dùng bàn chải cọ sạch các cặn phoi bùn (sludge) và màng sinh học bám dính. Lắp lại chặt chẽ để tránh bơm hút phải bọt khí.|**Áp dụng LOTO bước 1-3:** Ngắt CB điều khiển bơm. Đeo găng tay cao su. Khối lượng bơm khá nặng, chú ý tư thế nâng để không cụp cột sống.|
|**Bơm mỡ Mâm cặp**|Các vú mỡ (Grease nipples) trên mặt mâm cặp **8 inch**.|Sử dụng súng bơm mỡ, bơm định lượng vào tất cả các vú mỡ. Đạp bàn đạp chân (Foot Switch) cho ngàm đóng/mở 3-5 lần để mỡ bôi trơn tản đều vào cơ cấu Wedge Plunger bên trong, sau đó lau sạch mỡ thừa trào ra.|🛑 **CẢNH BÁO ĐỘNG LỰC HỌC TỪ CHƯƠNG 2:** BẮT BUỘC sử dụng mỡ chịu áp lực cao (High-pressure Chuck Grease) theo chuẩn nhà sản xuất. Nếu dùng mỡ màng mỏng thông thường, khi trục chính quay **4000 RPM**, lực ly tâm sẽ vắt kiệt mỡ ra ngoài. Cơ cấu Wedge mất bôi trơn sẽ kẹt, làm mất lực kẹp động. Hậu quả: Phôi **150kg** có thể văng ra khỏi ngàm như đạn pháo.|
|**Khe hở Đài dao**|Đài dao Servo 12 vị trí \& Khớp Curvic Coupling.|Quan sát khe hở giữa mâm dao và thân đài dao. Dùng cọ vệ sinh sạch mạt phoi bám quanh khe hở để đảm bảo quá trình Unclamp (nhả khớp) 0.2 giây không bị kẹt cơ học.|**Nguy cơ kẹp dập:** Thực hiện thao tác này khi máy ở chế độ E-Stop hoặc đã tắt NC Power để mâm dao không đột ngột xoay (Index) chém vào tay.|

### 5.1.3. Bảng bảo dưỡng Hàng tháng / 6 Tháng (Monthly / Semi-Annually)

Các hạng mục này yêu cầu Kỹ thuật viên bảo trì cấp cao thực hiện, áp dụng LOTO mức độ cao nhất.

|Hạng mục|Vị trí kiểm tra|Thao tác kỹ thuật chi tiết|Chú ý an toàn \& Cảnh báo (Safety Notes)|
|-|-|-|-|
|**Thay Dầu Thủy lực \& Vệ sinh HPU**|Trạm nguồn HPU (Thùng chứa **40 Lít**).|**(Định kỳ 6 tháng):** Hút bỏ toàn bộ 40L dầu cũ. Tháo nắp thùng, dùng giẻ không xơ (Lint-free cloth) lau sạch cặn kim loại dưới đáy. Thay mới lõi lọc đường hút và đường hồi. Đổ đúng 40L dầu thủy lực chống mài mòn chuẩn (VD: ISO VG 32 hoặc 46).|⚠️ **ÁP SUẤT BẪY (TRAPPED PRESSURE) - ĐỌC KỸ BƯỚC 5 LOTO:** Trước khi nới lỏng bất kỳ tuy-ô thủy lực nào, BẮT BUỘC phải dùng cờ lê xoay van cơ khí dự phòng trên van điện từ điều khiển mâm cặp và nòng ụ động. Việc này xả áp suất bẫy (đang bị giam lỏng ở mức **3.5 - 6.0 MPa** bởi van chống lún). Nếu bỏ qua, dầu sẽ xịt ra cắt đứt da hoặc nòng ụ động lao ra gây tai nạn.|
|**Kiểm tra Truyền động Trục chính**|Khoang động cơ trục chính (Phía trên thân máy).|**(Định kỳ hàng tháng):** Tháo nắp ốp bảo vệ. Kiểm tra bằng máy đo lực căng đai (Belt Tension Meter). Đai quá chùng gây trượt ở gia tốc cao; đai quá căng sẽ làm cháy cụm vòng bi P4. Kiểm tra bề mặt đai (Belt) không có vết nứt hay đứt gờ.|⚡ **NGUY HIỂM ĐIỆN ÁP DƯ:** LOTO Bước 5. Sau khi ngắt Cầu dao tổng, **BẮT BUỘC CHỜ 10 PHÚT** để điện trở xả tiêu thụ hết năng lượng. Đo lại hai cực DC Bus của Spindle Drive, xác nhận điện áp < 24VDC mới được thò tay vào khoang động cơ.|
|**Đo Điện trở Tiếp địa**|Tủ điện điều khiển \& Cọc tiếp địa ngoài trời.|**(Định kỳ 6 tháng):** Sử dụng máy đo điện trở đất chuyên dụng (Earth Tester) kẹp vào dây PE (cáp đồng tiết diện 14mm²) nối với Ground Busbar trong tủ điện. Đo giá trị điện trở từ cọc đồng tiếp địa độc lập lên máy.|⚡ **KIỂM SOÁT NHIỄU \& AN TOÀN:** Giá trị điện trở nối đất BẮT BUỘC phải **$< 10 \\ \\Omega$** (như quy định ở Chương 1). Nếu thông số này $> 10 \\ \\Omega$, hệ thống Servo số dễ bị mất bước do nhiễu vòng lặp (Ground Loop Noise), và quan trọng nhất, khung máy có thể tích điện giật chết người từ dòng rò 380/415VAC. Phải đóng thêm cọc tiếp địa hoặc xử lý lại hóa chất giảm điện trở đất ngay lập tức.|
|**Kiểm tra Mũi tâm Ụ động**|Nòng thủy lực (Quill) \& Mũi tâm quay MT4.|**(Định kỳ hàng tháng):** Tháo mũi tâm MT4 ra khỏi nòng Quill (đường kính 65mm). Vệ sinh sạch côn chuẩn MT4. Kiểm tra độ êm ái của vòng bi mũi tâm bằng tay.|Nếu vòng bi mũi tâm MT4 bị sượng, lực đẩy thủy lực **2.5 - 4.5 kN** từ nòng ụ động ép vào phôi đang quay 4000 RPM sẽ sinh nhiệt thiêu rụi cụm tâm, dẫn đến phá hủy chi tiết gia công (trọng lượng lên đến 300kg). Thay mũi tâm mới ngay nếu có dấu hiệu rơ lắc.|

### 5.1.4. Bảng bảo dưỡng Hàng năm (Annual / Đại tu)

Đây là cấp độ bảo dưỡng cao nhất, yêu cầu thiết bị phải dừng hoạt động từ 1-2 ngày. Khuyến cáo nên được thực hiện bởi đội ngũ Kỹ sư dịch vụ của hãng hoặc kỹ thuật viên cấp cao (Senior Maintenance Technician).

| Hạng mục | Vị trí kiểm tra | Thao tác kỹ thuật chi tiết | Chú ý an toàn & Cảnh báo (Safety Notes) |
| :--- | :--- | :--- | :--- |
| **Đo kiểm Dung sai hình học (Leveling & Geometry)** | Băng máy 45 độ, Trục chính, Cụm Ụ động. | Sử dụng thước thủy tĩnh điện tử (Precision Level) để đo lại độ thăng bằng của máy. Cân chỉnh lại các chân đế (Leveling pads) nếu có sự sụt lún nền móng. Chạy bài kiểm tra Ballbar Test để hiệu chuẩn lại độ nội suy tròn của trục X/Z, bù trừ độ rơ vít me bi. | ⚠️ **An toàn bệ máy:** Không tháo dỡ các bu lông neo móng (Anchor bolts) nếu không có dụng cụ đỡ chịu tải. |
| **Thay Pin dự phòng Bộ nhớ (CNC & Servo Battery)** | Tủ điện điều khiển trung tâm (CNC Controller & Servo Amplifiers). | Thay mới toàn bộ pin Lithium dự phòng nuôi bộ nhớ RAM của bo mạch chủ và hệ thống Absolute Encoder. **BẮT BUỘC** thao tác khi máy **ĐANG BẬT ĐIỆN (Power ON)**. | ⚡ **NGUY HIỂM ĐIỆN GIẬT:** Thao tác khi máy đang có điện 380V/415V và DC Bus 600V. Bắt buộc đeo găng tay cách điện chuyên dụng. Tránh làm rơi ốc vít vào bo mạch gây chập cháy. |
| **Thay thế Dây đai truyền động (Drive Belts)** | Khoang động cơ trục chính (Spindle Motor). | Thay mới toàn bộ bộ dây đai truyền động dù chưa đứt để đảm bảo không bị giãn, trượt hoặc mất mô-men xoắn ở tốc độ tối đa 4000 RPM. Dùng máy đo lực căng đai để thiết lập độ căng chuẩn. | Thực hiện triệt để **Quy trình LOTO Bước 5** (Chờ xả áp điện trở 10 phút trước khi chạm vào cụm động cơ). |
| **Thay thế Phớt gạt bụi (Wiper/Scraper)** | Tấm che Telescopic trục X/Z. | Tháo các tấm che bảo vệ băng trượt. Thay thế hệ thống phớt gạt mạt kim loại và dung dịch làm mát. | Phớt hỏng sẽ làm mạt phoi lọt vào phá hủy cụm vòng bi cấp C3 của vít me bi và ray trượt con lăn. |

## 5.2. Bảng tra cứu mã lỗi và Xử lý sự cố (Troubleshooting) - Phần Cơ khí \& Thủy lực

Khi máy tiện CNC-L200 phát sinh sự cố, bộ điều khiển trung tâm (NC Controller) sẽ ngay lập tức khóa mọi chuyển động và hiển thị mã lỗi (Alarm Code) trên màn hình HMI. Kỹ thuật viên tuyệt đối không được nhấn nút "RESET" để cố tình chạy tiếp khi chưa xác định được nguyên nhân gốc rễ, hành động này có thể dẫn đến phá hủy hoàn toàn cụm cơ khí.

Quy trình chuẩn tắc xử lý sự cố luôn phải tuân theo trình tự: **Đọc mã lỗi -> Nhận diện Hiện tượng -> Phân tích Nguyên nhân gốc rễ -> Khắc phục (Có áp dụng LOTO).**

### 5.2.1. AL-201: Lỗi kẹt đài dao / Đài dao không quay (Turret Indexing Error)

* **Hiện tượng:**
Khi thực thi lệnh gọi dao (VD: `T0303`) trên chế độ MDI hoặc AUTO, máy phát ra cảnh báo AL-201. Từ buồng máy, có thể nghe thấy tiếng cạch của rơ-le hoặc tiếng động cơ gằn lên nhưng mâm dao 12 vị trí không xoay, xoay rất chậm, hoặc xoay nhưng chốt lại sai vị trí mục tiêu.
* **Nguyên nhân gốc rễ:**

  1. **Tụt áp suất thủy lực nhả khớp:** Để Servo có thể quay trong 0.2 giây, áp suất thủy lực phải đẩy mâm dao trượt ra 5mm để nhả khớp răng Curvic Coupling (Unclamp). Nếu áp suất nhánh này tụt dưới **3.5 MPa**, các răng xéo không tách rời hoàn toàn, dẫn đến kẹt cơ khí. Động cơ Servo bị quá tải khi cố quay.
  2. **Kẹt phoi cơ học:** Phoi cắt siêu nhỏ lọt qua khe hở của mâm dao, chèn vào giữa các rãnh của khớp nối 3 mảnh Curvic Coupling, cản trở việc khóa/nhả khớp.
  3. **Lỗi cụm van điện từ (Solenoid Valve):** Khí nén cấp vào hệ thống thổi sạch đài dao không đạt chuẩn (lẫn hơi nước do không xả cụm FRL **0.6 - 0.8 MPa** hàng ngày). Nước đi vào làm rỉ sét lõi van điện từ, khiến van kẹt ở trạng thái lơ lửng, thủy lực không thể đảo chiều.
* **Cách khắc phục chi tiết:**

  1. **Kiểm tra thông số:** Đứng ngoài máy, nhìn đồng hồ trạm HPU xem áp suất có duy trì ở dải **3.5 - 6.0 MPa** hay không. Kiểm tra van điện từ đài dao có sáng đèn tín hiệu khi gọi dao không.
  2. **Bắt buộc áp dụng LOTO 5 Bước:** Ngắt Machine Power, tắt Cầu dao tổng.

     * ⚡ *Cảnh báo điện áp dư:* Chờ đúng 10 phút, dùng đồng hồ đo điện áp trên tụ DC Bus của Servo Drive trục X/Z đảm bảo < 24VDC.
     * ⚠️ *Cảnh báo cơ học rơi tự do:* Dùng khối gỗ hoặc đội thủy lực kê dưới mâm đài dao trước khi ngắt áp lực, vì khi mất áp suất và Servo nhả phanh, đài dao mất cân bằng sẽ rơi tự do chém xuống băng máy.
  3. **Vệ sinh cơ khí:** Xả áp suất bẫy thủy lực tại trạm van. Tháo nắp ốp mặt trước của đài dao. Rút cụm mâm dao ra ngoài. Dùng dung dịch RP7 rửa sạch cặn phoi kẹt trong các răng xéo của khớp Curvic Coupling. Bôi một lớp mỡ mỏng và lắp ráp lại.

### 5.2.2. AL-304: Áp suất mâm cặp / Ụ động tụt thấp (Hydraulic Pressure Drop)

* **Hiện tượng:**
Đang gia công, màn hình bất ngờ chớp đỏ AL-304. Máy ngay lập tức chuyển sang trạng thái Feed Hold (Dừng bước tiến dao trục X/Z) và phanh dừng khẩn cấp Trục chính. Đồng hồ áp suất thủy lực tổng tụt xuống dưới mức an toàn (< 3.5 MPa). Cơ chế bảo vệ này được kích hoạt để ngăn chặn thảm họa văng phôi (do mất lực kẹp) khi máy đang chạy tốc độ cao.
* **Nguyên nhân gốc rễ:**

  1. **Cạn môi chất:** Dầu thủy lực trong thùng **40 Lít** tụt xuống dưới mức báo động do không châm thêm hoặc rò rỉ ngầm kéo dài, khiến bơm hút phải không khí (e khí).
  2. **Rò rỉ Xylanh xoay (Rotary Cylinder):** Phớt làm kín (Oil seal) bên trong Xylanh xoay ở đuôi trục chính bị rách do chạy liên tục ở 4000 RPM với dầu bẩn, khiến áp suất bị xả thẳng về đường hồi.
  3. **Kẹt van chống lún Ụ động:** Van một chiều (Pilot-operated check valve) bảo vệ nòng ụ động bị kẹt cặn bẩn, rò rỉ áp suất bên trong hệ thống xylanh nòng.
* **Cách khắc phục chi tiết:**

  1. **Xử lý nhanh:** Kiểm tra mắt trâu thùng HPU. Nếu hết dầu, châm ngay dầu ISO VG 32/46 cho đủ 40 Lít và xả e đường ống.
  2. **Kiểm tra rò rỉ đuôi máy:** Mở cửa che phía sau trục chính, quan sát gầm cụm Rotary Cylinder. Nếu thấy dầu thủy lực rỉ thành giọt lớn hoặc phun sương, bắt buộc phải tháo cụm xylanh này ra để thay bộ phớt (Seal kit) chịu tốc độ cao.
  3. **Khắc phục van ụ động \& ⚠️ CẢNH BÁO TỬ VONG (ÁP SUẤT BẪY):** Nếu rò rỉ nằm ở cụm van điều khiển nòng ụ động, tuyệt đối KHÔNG ĐƯỢC cầm cờ lê tháo cút nối thủy lực ngay. Mặc dù bơm HPU đã tắt, van chống lún vẫn đang giam lỏng một lượng áp suất bẫy cực cao (lên tới 6.0 MPa) bên trong cụm nòng.

     * *Thao tác sống còn:* Bắt buộc dùng cờ lê xoay chốt **Manual Override** trên thân van điện từ để xả sạch áp suất bẫy này (quan sát đồng hồ nhánh phải tụt về 0 MPa) trước khi tháo bất kỳ con ốc nào. Nếu bỏ qua, tia dầu 6.0 MPa sẽ bắn ra cắt đứt da thịt hoặc nòng ụ động phóng ra phía trước nghiền nát tay kỹ thuật viên.

### 5.2.3. Cảnh báo rung động bất thường Trục chính (Spindle Excessive Vibration)

* **Hiện tượng:**
Không có mã lỗi điện tử, nhưng người vận hành nghe thấy tiếng rít (squeal) chói tai hoặc tiếng ù ầm ĩ khi trục chính tăng tốc lên dải 3000 - 4000 RPM. Bề mặt chi tiết tiện tinh không sáng bóng mà xuất hiện các vết vằn vện, gợn sóng (lỗi vảy cá - Chatter marks).
* **Nguyên nhân gốc rễ:**

  1. **Mất lực kẹp động lực học do thiếu mỡ:** Mâm cặp 8 inch không được bơm đúng loại mỡ chịu áp lực cao hàng tuần. Ở 4000 RPM, lực ly tâm thắng lực kéo của cơ cấu Wedge Plunger đang bị kẹt do ma sát khô. Ngàm kẹp lỏng ra không đều, gây mất cân bằng động (Imbalance) sinh ra rung chấn.
  2. **Vi phạm tỷ lệ chiều dài phôi (L/D > 3):** Gá phôi quá dài (ví dụ phôi dài 200mm, đường kính chỉ 50mm) lơ lửng trên mâm cặp (đạt giới hạn 150kg) mà **không** sử dụng nòng ụ động để chống tâm. Lực đẩy dao (Cutting force) làm phôi bị uốn cong, quật (whipping) và rung bần bật trong lúc tiện.
  3. **Thoái hóa vòng bi trục chính:** Trục chính đã va chạm mạnh (Crash) hoặc chạy quá tải lâu ngày làm xước/vỡ rọ bi của cụm vòng bi tiếp xúc góc siêu chính xác lớp P4.
* **Cách khắc phục chi tiết:**

  1. **Bảo dưỡng mâm cặp:** Dừng máy ngay lập tức. Bơm đầy mỡ chịu áp lực cao vào các vú mỡ. Đạp bàn đạp đóng/mở ngàm liên tục để mỡ bôi trơn lại toàn bộ cơ cấu Wedge bên trong, phục hồi lực kẹp tĩnh và động.
  2. **Thiết lập lại Ụ động chống tâm (Tailstock Support):** Nếu tỷ lệ L/D > 3, BẮT BUỘC phải kéo thân ụ động vào vị trí. Kích hoạt nòng thủy lực (Quill) với mũi tâm chuẩn MT4 đẩy vào lỗ tâm phôi. Điều chỉnh van áp suất nhánh ụ động đạt mức **3.5 - 6.0 MPa**. Lúc này, nòng ụ động sẽ tạo ra một lực đẩy hằng số từ **2.5 - 4.5 kN**, vừa dập tắt hoàn toàn dao động uốn của phôi, vừa có khả năng thụt lùi siêu vi mô để bù trừ biến dạng nhiệt của phôi thép.
  3. **Đo kiểm vòng bi P4:** Nếu đã làm 2 bước trên mà vẫn rung, dùng đồng hồ so (Dial indicator) đo độ đảo mặt đầu (Runout) và độ rơ hướng kính của mũi trục chính chuẩn A2-6. Nếu độ đảo vượt quá $0.005 \\text{ mm}$, vòng bi P4 đã hỏng. *Lưu ý:* Việc tháo lắp thay thế vòng bi P4 yêu cầu phòng sạch và kỹ sư chuyên hãng, nhà máy tuyệt đối không tự ý dùng búa đóng/ép tháo cụm trục chính.

### 5.2.4. AL-105: Quá tải động cơ Servo / Vượt quá hành trình cứng (Overtravel / Servo Overload)

* **Hiện tượng:**
Trục X hoặc trục Z đang di chuyển (đặc biệt trong lúc chạy dao nhanh G00) thì máy đột ngột dừng sập lại kèm theo chấn động mạnh. Màn hình HMI chớp đỏ mã lỗi AL-105. Kiểm tra bên trong tủ điện, bộ khuếch đại Servo (Servo Amplifier) của trục tương ứng báo lỗi quá dòng (Overcurrent).
* **Nguyên nhân gốc rễ:**

  1. **Đâm sầm cơ học (Crash):** Do kỹ thuật viên nhập sai giá trị bù dao (Tool Offset) hoặc gọi nhầm dao, khiến đài dao lao thẳng vào mâm cặp hoặc nòng ụ động ở tốc độ tối đa (Trục X = 24 m/phút, Trục Z = 30 m/phút).
  2. **Kẹt cơ khí:** Phoi cắt kim loại không được dọn sạch, bám két và lọt qua phớt chắn bụi che băng máy, kẹt chặt vào bên trong thanh ray dẫn hướng tuyến tính loại con lăn hoặc kẹt vào bước ren của cụm vít me bi cấp C3, làm đứng khựng hệ thống truyền động.
  3. **Lố hành trình:** Máy chạy vượt qua công tắc giới hạn hành trình mềm và đè lên công tắc giới hạn hành trình cứng (Hard Limit Switch).
* **Cách khắc phục chi tiết:**

  1. 🛑 **Cảnh báo thao tác:** Trong khoảnh khắc máy đang bị kẹt cứng (Crash), **Tuyệt đối KHÔNG sử dụng nút E-Stop hoặc tắt Machine Power**. Việc cắt điện lúc này sẽ làm phanh từ (Magnetic Brake) trên động cơ trục X (trục chịu trọng lực) đóng sập lại, khóa chết vị trí kẹt. Đồng thời, mất nguồn Servo sẽ làm mất khả năng lùi dao có kiểm soát.
  2. **Giải phóng ứng suất:** Chuyển núm chọn chế độ sang **HANDLE** (Tay quay MPG). Vặn núm chia độ về bước vi mô nhỏ nhất (**0.01 mm hoặc 0.001 mm**). Chậm rãi quay núm MPG *ngược lại* với hướng vừa va chạm để từ từ lùi đài dao ra, giải phóng ứng suất xoắn đang đè nặng lên vít me bi và Servo.
  3. **Kiểm tra hư hại:** Sau khi lùi đài dao ra vùng an toàn, kỹ thuật viên bảo trì phải sử dụng đồng hồ so (Dial indicator) để rà lại độ song song của trục Z và độ vuông góc của trục X. Va chạm ở tốc độ 24-30 m/phút có khả năng lớn làm lệch hình học của băng máy Meehanite và hỏng cụm vòng bi đỡ vít me.

### 5.2.5. AL-500: Lỗi đồng bộ tọa độ / Yêu cầu Zero Return (Zero Return Incomplete)

* **Hiện tượng:**
Lỗi này thường xuất hiện sau khi xưởng bị cúp điện lưới đột ngột, hoặc ngay sau khi người vận hành nhả nút E-Stop. Màn hình CNC báo AL-500, máy từ chối chạy chế độ AUTO và yêu cầu người dùng xác lập lại tọa độ gốc của hệ thống.
* **Nguyên nhân gốc rễ:**

  1. **Trôi cơ học:** Cỗ máy sử dụng hệ thống Absolute Encoder (Encoder tuyệt đối) cho cả trục X và Z. Khi cúp điện hoặc nhấn E-Stop, phanh từ đóng lại bằng lực cơ học giật cục, có thể làm trục vít me bị "trôi" đi một khoảng siêu vi mô. Lúc này, tọa độ vật lý bị lệch so với tọa độ được lưu trong bộ nhớ RAM của CNC, vi xử lý sẽ báo lỗi để tránh gia công sai kích thước.
  2. **Suy giảm nguồn Pin Servo:** Pin nuôi bộ nhớ vị trí cho Encoder tuyệt đối (thường nằm trên bộ Servo Drive trong tủ điện) đã cạn kiệt, khiến tọa độ gốc bị xóa trắng khi mất điện AC.
* **Cách khắc phục chi tiết:**

  1. **Đưa máy về gốc chuẩn tắc:** Chuyển hệ thống sang chế độ REF (Zero Return).
⚠️ **NHẮC LẠI CẢNH BÁO TỬ HUYỆT (Từ Chương 4):** BẮT BUỘC phải nhấn nút **(+X)** trước để nâng toàn bộ cụm đài dao lên vị trí cao nhất, tránh xa vùng va chạm. Chỉ khi đèn báo X Zero sáng lên, mới được phép nhấn nút **(+Z)** để đưa trục Z về gốc. Nếu làm ngược lại (đưa Z về trước), đài dao có thể quét ngang và đâm sầm vào nòng ụ động.
  2. **Thay pin định kỳ:** Nếu lỗi do pin, tiến hành tháo nắp tủ điện và thay pin Servo. **Lưu ý đặc biệt:** Việc thay pin Servo phải được thực hiện khi máy **ĐANG BẬT ĐIỆN (Power ON)** để bo mạch không bị mất hoàn toàn dữ liệu Encoder. Thợ điện phải mang găng tay cách điện và cực kỳ cẩn trọng với điện áp DC Bus kế bên.

### 5.2.6. AL-901: Lỗi truyền thông Board mạch / Nhiễu tín hiệu (System Hang / Communication Error)

* **Hiện tượng:**
Đang gia công, màn hình điều khiển CNC bất ngờ bị đơ cứng (treo máy), các phím bấm vật lý không có phản hồi. Hoặc máy hiển thị dòng báo lỗi mất kết nối cáp quang (FSSB / Optical Fiber) giữa Board mạch điều khiển chủ (NC) và các Module biến tần Servo.
* **Nguyên nhân gốc rễ:**
Hệ thống bo mạch kỹ thuật số và cáp quang trên CNC-L200 vô cùng nhạy cảm với chất lượng hạ tầng điện (đã được cảnh báo nghiêm ngặt ở Chương 1).

  1. **Sụt áp lưới điện:** Điện áp xoay chiều 3 pha (380V/415V) của nhà xưởng dao động vượt quá ngưỡng dung sai cho phép **$\\pm 10%$**. Điều này thường xảy ra nếu máy CNC được đấu chung đường dây với các thiết bị sinh xung lực lớn (như máy dập, búa máy, máy hàn công nghiệp lớn).
  2. **Nhiễu vòng lặp nối đất (Ground Loop Noise):** Dây tiếp địa bị lỏng, đứt ngầm, hoặc chất lượng cọc tiếp địa ngoài trời bị suy giảm khiến điện trở nối đất tăng vọt (lớn hơn $10 \\Omega$). Khi đó, các luồng nhiễu điện từ (EMI) sinh ra từ biến tần ở tốc độ 4000 RPM không xả được xuống đất, dội ngược lên bo mạch chủ làm treo vi xử lý.
* **Cách khắc phục chi tiết:**

  1. **Kiểm tra nguồn 3 pha:** Dùng đồng hồ VOM đo điện áp tại cầu dao tổng (phía Line side). Nếu phát hiện điện áp trồi sụt liên tục vượt ngưỡng $\\pm 10%$, bắt buộc phải ngừng chạy máy. Tiến hành lắp đặt ngay một Bộ ổn áp tự động (AVR) với công suất tối thiểu **30 kVA** chuyên dụng cho máy CNC.
  2. **Kiểm tra rào chắn tiếp địa:** Gọi kỹ sư điện dùng máy đo chuyên dụng (Earth Resistance Tester) đo lại cọc tiếp địa độc lập (Class 3) của máy. Giá trị thu được BẮT BUỘC phải **$< 10 \\Omega$** (lý tưởng là $< 4 \\Omega$). Nếu không đạt, phải nhồi thêm hóa chất giảm điện trở đất (GEM) hoặc đóng thêm cọc đồng. Đồng thời, siết lại cáp đồng tiếp địa ($14 \\text{ mm}^2$) nối vào Ground Busbar trong tủ điện.
⚡ *Cảnh báo:* Tuyệt đối không cố tình "khởi động lại chạy tạm" khi hệ thống tiếp địa đang bị lỗi, vì không chỉ gây hỏng dàn Board mạch đắt tiền mà còn đe dọa sinh mạng người thao tác do rò rỉ điện.

## 5.3. Bảng tra cứu mã lỗi và Xử lý sự cố - Phần Phần mềm, Lập trình & Cảm biến

Ngoài các lỗi cơ học, hệ thống cảm biến an toàn và vi xử lý nội suy cũng có thể phát sinh cảnh báo khóa máy.

### 5.3.1. AL-010 / AL-011: Lỗi cú pháp G-Code hoặc Sai định dạng (Program Syntax Error)
* **Hiện tượng:** Máy dừng chạy ngay lập tức khi đang ở chế độ AUTO. Màn hình báo lỗi màu vàng (Warning) thay vì màu đỏ. Trục chính vẫn có thể đang quay nhưng các trục X/Z dừng tiến dao.
* **Nguyên nhân gốc rễ:** 
  1. Lỗi đánh máy trong chương trình gia công (ví dụ: gõ `G0` thay vì `G00`, hoặc quên dấu chấm thập phân `X50` thay vì `X50.0`).
  2. Xung đột lệnh bù trừ bán kính dao (G41/G42) khi di chuyển vào một góc bo (Radius) nhỏ hơn bán kính chíp dao đã khai báo.
* **Cách khắc phục:** Chuyển sang chế độ **EDIT**, kiểm tra lại dòng lệnh bị lỗi (khối block được bôi sáng trên màn hình). Sửa lại cú pháp G-Code hoặc thiết lập lại bán kính mũi dao (Cột R) trong bảng Offset.

### 5.3.2. AL-112: Lỗi công tắc cửa an toàn (Door Interlock / Safety Guard Open)
* **Hiện tượng:** Không thể khởi động trục chính hoặc chạy dao tự động. Nhấn Cycle Start máy không phản hồi và báo lỗi AL-112.
* **Nguyên nhân gốc rễ:**
  1. Cửa buồng máy chưa được đóng kín hoàn toàn.
  2. Mạt kim loại bám vào nam châm của cảm biến từ ở mép cửa, hoặc chốt khóa cơ điện (Solenoid Interlock) bị kẹt do thiếu bôi trơn.
* **Cách khắc phục:** 
  1. Vệ sinh sạch mép cửa và cảm biến từ/chốt khóa cơ khí. Đóng lại cửa dứt khoát.
  2. 🛑 **CẤM KỴ:** Tuyệt đối KHÔNG ĐƯỢC đấu tắt (Bypass) dây tín hiệu cảm biến cửa để chạy máy khi mở cửa. Đây là hành vi vi phạm an toàn nghiêm trọng, loại bỏ lớp rào chắn duy nhất bảo vệ người vận hành khỏi phoi văng và nguy cơ cuốn ép.

### 5.3.3. AL-401: Quá tải nhiệt / Quá nhiệt biến tần (Servo / Spindle Overheat)
* **Hiện tượng:** Máy báo lỗi và từ chối tăng tốc độ trục chính, hoặc dừng đột ngột sau thời gian gia công cắt gọt nặng liên tục.
* **Nguyên nhân gốc rễ:** 
  1. Môi trường đặt máy vượt quá 40°C (Vi phạm yêu cầu môi trường ở Chương 1).
  2. Tấm lọc bụi (Dust filter) trên quạt tản nhiệt của tủ điện bị nghẹt cứng bám đầy mạt kim loại và hơi dầu (Oil mist), làm quạt không thể hút gió làm mát các tấm Heat sink của biến tần.
* **Cách khắc phục:** Dừng máy. Tháo các tấm lọc bụi ở hai bên hông tủ điện mang đi giặt sạch bằng khí nén hoặc nước (phơi khô trước khi lắp). Đảm bảo điều hòa nhà xưởng hoặc hệ thống thông gió tủ điện hoạt động tốt. Reset lại máy sau khi nhiệt độ tản nhiệt hạ xuống dưới 45°C.