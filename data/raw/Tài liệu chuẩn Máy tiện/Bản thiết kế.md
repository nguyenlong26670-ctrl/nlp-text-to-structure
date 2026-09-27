# TÀI LIỆU ĐẶC TẢ KỸ THUẬT THIẾT KẾ CHI TIẾT (DESIGN SPECIFICATION)
**Dự án:** Máy tiện CNC-L200
**Người lập:** Kỹ sư trưởng thiết kế cơ khí

---

## 1. Cấu trúc khung bệ máy (Machine Bed Structure)

Khung bệ máy là nền tảng cơ học cốt lõi, quyết định độ chính xác hình học và khả năng hấp thụ rung động của toàn bộ hệ thống. Thiết kế khung bệ của CNC-L200 sử dụng vật liệu đúc nguyên khối kết hợp cấu trúc mạng gân gia cường chữ X (X-ribs) bên trong lòng khối đúc, nhằm chống lại lực vặn xoắn (Torsion) sinh ra trong quá trình cắt gọt hạng nặng.

Băng máy được thiết kế góc nghiêng giúp tối ưu hóa động lực học phoi cắt (Chip Flow), ngăn chặn sự tích tụ phoi nóng đỏ gây giãn nở nhiệt cục bộ. Đồng thời, thiết kế này cải thiện công thái học, giúp trục chính tiến sát người vận hành, giảm nguy cơ tai nạn cuốn ép.

**Bảng 1.1: Thông số vật lý và kích thước khung bệ**

| Hạng mục thiết kế | Đơn vị | Giá trị / Vật liệu |
| :--- | :--- | :--- |
| Vật liệu đúc khung bệ chính | - | Gang Meehanite (Meehanite cast iron) |
| Góc nghiêng băng máy (Slant bed angle) | Độ (Degree) | $45$ |
| Trọng lượng tịnh (Net Weight) | $\text{kg}$ | $4200$ |
| Chiều dài tổng thể (Không gồm băng tải phoi) | $\text{mm}$ | $2550$ |
| Chiều rộng tổng thể | $\text{mm}$ | $1650$ |
| Chiều cao tổng thể | $\text{mm}$ | $1850$ |
| Chiều cao tâm trục chính (Từ mặt sàn) | $\text{mm}$ | $1050$ |
| Kích thước bu lông neo móng (Anchor bolts) | $\text{mm}$ | TBD (To Be Determined) |
| Lực siết bu lông neo móng | $\text{N.m}$ | TBD (To Be Determined) |

---

## 2. Tiêu chuẩn nền móng và Chống rung chấn (Foundation & Anti-Vibration)

Với khối lượng tĩnh lớn và mô-men xoắn cao sinh ra từ trục chính, nền móng lắp đặt máy phải đáp ứng các tiêu chuẩn khắt khe về dân dụng để tránh hiện tượng sụt lún, vặn xoắn thân máy theo thời gian. Nếu phát hiện gia tốc rung chấn từ môi trường xung quanh vượt ngưỡng cho phép, đội ngũ thiết kế nhà xưởng bắt buộc phải bổ sung mương chống rung cách ly hoàn toàn cỗ máy.

**Bảng 1.2: Đặc tả kỹ thuật nền móng bê tông và Mương chống rung**

| Thông số nền móng | Đơn vị | Giá trị / Chuẩn giới hạn |
| :--- | :--- | :--- |
| Mác bê tông cốt thép tối thiểu | - | Từ M300 (C30) trở lên |
| Độ dày lớp bê tông tối thiểu | $\text{mm}$ | $\ge 300$ ($12 \text{ inches}$) |
| Tiêu chuẩn cốt thép đan móng | - | Tối thiểu 2 lớp thép $\phi 12$ (D12) |
| Khả năng chịu tải bề mặt tối thiểu | $\text{kg/m}^2$ | $> 5000$ |
| Độ võng bề mặt tối đa (Trên $3\text{m}$ chiều dài) | $\text{mm}$ | $5$ |
| Gia tốc rung chấn môi trường cần đào mương | $\text{G}$ | $> 0.5$ |
| Độ sâu tối thiểu của mương chống rung | $\text{mm}$ | $600$ |
| Độ rộng của mương chống rung | $\text{mm}$ | $100$ |
| Vật liệu lấp mương chống rung | - | Cát khô, mùn cưa, hoặc đệm cao su Neoprene |
| Độ dốc rãnh thu hồi dung dịch làm mát | $\%$ | $1\% - 2\%$ |

**Bảng 1.3: Bố trí không gian an toàn (Safety Clearances)**
*(Khoảng trống phục vụ bảo dưỡng, LOTO và thoát hiểm)*

| Vị trí giới hạn | Đơn vị | Khoảng cách tối thiểu |
| :--- | :--- | :--- |
| Phía sau máy (Tủ điện, cầu dao tổng) | $\text{mm}$ | $1000$ |
| Phía hông đổ phoi (Khu vực băng tải) | $\text{mm}$ | $1500$ |
| Phía trước máy (Vùng vận hành chính) | $\text{mm}$ | $1000$ |
| Phía hông còn lại (Cụm FRL, Bơm làm mát) | $\text{mm}$ | $1000$ |

---

## 3. Yêu cầu Môi trường và Năng lượng (Environment & Power Requirements)

Hệ thống điều khiển CNC, Servo Amplifier và các cảm biến quang/từ tính yêu cầu môi trường làm việc ổn định. Sự thay đổi nhiệt độ đột ngột sẽ phá vỡ độ chính xác gia công do hiện tượng giãn nở nhiệt. Hệ thống tiếp địa đóng vai trò bảo vệ tín hiệu kỹ thuật số và tính mạng người vận hành khỏi điện áp rò rỉ (lên tới $600\text{VDC}$ từ tụ điện DC Bus hoặc $380\text{VAC}$ từ lưới điện).

**Bảng 1.4: Giới hạn nhiệt độ, Độ ẩm và Năng lượng**

| Yêu cầu kỹ thuật | Đơn vị | Giá trị giới hạn / Tiêu chuẩn |
| :--- | :--- | :--- |
| Nhiệt độ môi trường cho phép | $^\circ \text{C}$ | $10 - 40$ ($50^\circ \text{F} - 104^\circ \text{F}$) |
| Nhiệt độ tối ưu cho độ chính xác | $^\circ \text{C}$ | $20 \pm 2$ |
| Biến thiên nhiệt độ tối đa | $^\circ \text{C}/\text{giờ}$ | $\le 1$ |
| Độ ẩm tương đối (Không đọng sương) | $\%$ | $30 - 75$ |
| Tổng công suất điện yêu cầu | $\text{kVA}$ | $30$ |
| Điện áp cung cấp (3 Pha 4 Dây - 3P+PE) | $\text{VAC}$ | $380$ hoặc $415$ |
| Tần số dòng điện | $\text{Hz}$ | $50$ hoặc $60$ ($\pm 1$) |
| Biến thiên điện áp tối đa cho phép | $\%$ | $\pm 10$ |
| Mất cân bằng pha tối đa | $\%$ | $\le 5$ |
| Công suất tối thiểu của Bộ ổn áp (AVR) | $\text{kVA}$ | $30$ (Bắt buộc nếu biến thiên $> 10\%$) |
| Điện trở nối đất (Cọc tiếp địa độc lập) | $\Omega$ | $\le 10$ (Tối ưu $< 4$) |
| Tiết diện cáp đồng PE bọc PVC tối thiểu | $\text{mm}^2$ | $14$ (AWG 6) |

---

## 4. Đánh dấu giới hạn rủi ro cơ học & Điểm kẹp dập (Pinch Points & Safety Markings)

Bộ phận thiết kế CAD 3D BẮT BUỘC phải trích xuất các vị trí sau trên bản vẽ lắp ráp tổng thể, chỉ định rõ vùng rủi ro để dán nhãn an toàn (Safety Decals) đạt chuẩn quốc tế ISO 7010.

*   **Rủi ro kẹp dập cơ học / Nguy cơ nghiền nát (ISO 7010-W024):** Các vị trí này có vận tốc di chuyển tuyến tính cực lớn, lực ép có thể đạt vài tấn.
    *   **Vị trí 1:** Dọc theo các tấm che băng trượt (Telescopic Way Covers) của trục Z và trục X.
    *   **Vị trí 2:** Ray trượt của cửa bảo vệ chính (Automatic Front Door).
*   **Rủi ro nhiệt độ cao / Nguy cơ bỏng nhiệt (ISO 7010-W017):** Các bề mặt sinh nhiệt trong chu kỳ tải nặng.
    *   **Vị trí 3:** Khu vực tản nhiệt (Heat sink) của Tủ điện (đặt sau khung máy).
*   **Rủi ro không gian hẹp & Va đập (Crash Hazard):**
    *   **Vị trí 4:** Không gian chết giữa đài dao và băng máy, đặc biệt lưu lưu ý nguy cơ sập đài dao chém vào băng máy khi tháo rời động cơ trục X mà không chèn khối chặn cơ khí (Mechanical Blocks).

> **Ghi chú cho nhóm 3D:** Tuyệt đối không thiết kế các cơ cấu gờ nổi hoặc ống dẫn đi ngang qua các khoảng hở (Clearances) $1000\text{mm} - 1500\text{mm}$ đã quy định, nhằm giữ lối thoát hiểm vô điều kiện cho kỹ thuật viên khi xảy ra sự cố phóng hồ quang điện (Arc Flash).

---

## 5. Module 2: Động lực học Cụm Trục chính và Mâm cặp (Spindle & Chuck Dynamics)

Cụm Trục chính và Mâm cặp là "trái tim" của máy CNC-L200, nơi diễn ra sự chuyển hóa năng lượng điện thành động năng cắt gọt hạng nặng. Yêu cầu thiết kế của cụm này phải thỏa mãn đồng thời hai yếu tố: Độ cứng vững động lực học ở tốc độ cao và kiểm soát triệt để lực ly tâm để duy trì kẹp phôi an toàn.

### 5.1. Đặc tả kỹ thuật Cụm Trục chính (Spindle Assembly)

Trục chính sử dụng động cơ AC Spindle công suất lớn, kết hợp hệ thống vòng bi tiếp xúc góc siêu chính xác để triệt tiêu độ đảo (Runout). Do sinh nhiệt lớn khi vận hành ở tốc độ tối đa $4000 \text{ RPM}$, bộ phận CAD/CAE phải tích hợp không gian cho hệ thống áo nước/dầu làm mát tuần hoàn. Hệ thống phần mềm CNC sẽ khóa trần (Clamp parameter) tốc độ này để ngăn chặn vượt ngưỡng cơ học.

**Bảng 2.1: Thông số vật lý và Giới hạn vận hành Trục chính**

| Hạng mục thiết kế | Đơn vị | Giá trị / Vật liệu / Chuẩn giới hạn |
| :--- | :--- | :--- |
| Tốc độ quay lớn nhất (Max Speed) - Giới hạn phần mềm | $\text{Vòng/phút (RPM)}$ | $4000$ |
| Công suất động cơ (Liên tục / Định mức 30 phút) | $\text{kW}$ | $11 / 15$ |
| Mô-men xoắn tối đa (Max Torque) | $\text{N.m}$ | $167$ |
| Chuẩn mũi trục chính (Spindle Nose) | - | A2-6 |
| Đường kính vòng bi trục chính | $\text{mm}$ | $100$ |
| Chuẩn vòng bi (Angular contact bearings) | - | Lớp siêu chính xác P4 |
| Đường kính lỗ lọt phôi tối đa qua trục (Bar capacity) | $\text{mm}$ | $52$ |
| Độ đảo mặt đầu tối đa cho phép (Runout limit) | $\text{mm}$ | $< 0.005$ |
| Năng lượng tích tụ ngầm (Tụ DC Bus biến tần) | $\text{VDC}$ | Lên tới $600$ (Xả trong $> 10$ phút) |
| Hệ thống kiểm soát nhiệt độ trục | - | Áo nước/dầu tuần hoàn (Spindle Chiller System) |
| Loại đai truyền động (Drive Belt) | - | TBD (To Be Determined) |
| Lực căng đai tiêu chuẩn | $\text{N}$ | TBD (To Be Determined) |

### 5.2. Động lực học Mâm cặp & Xylanh xoay (Chuck & Rotary Cylinder)

Cơ cấu kẹp sử dụng Xylanh xoay lắp ở đuôi trục chính, truyền lực kéo dọc qua tâm bằng ống Drawtube làm từ thép cường lực đến cơ cấu chêm trượt (Wedge Plunger) bên trong mâm cặp. Chêm trượt chuyển đổi chuyển động tịnh tiến thành chuyển động xuyên tâm, ép chặt ngàm vào phôi.
Kỹ sư thiết kế phải tính đến sự suy giảm lực kẹp động (Dynamic Grip Loss) do lực ly tâm ($F = m \cdot \omega^2 \cdot r$) sinh ra ở vận tốc $4000 \text{ RPM}$, lực này sẽ hướng ra ngoài, đi ngược lại lực ép thủy lực $30-40\text{ kN}$ ban đầu.

**Bảng 2.2: Thông số Động lực học kẹp phôi**

| Hạng mục thiết kế | Đơn vị | Giá trị / Vật liệu / Chuẩn giới hạn |
| :--- | :--- | :--- |
| Loại mâm cặp | - | Thủy lực (Hydraulic Chuck) |
| Kích thước mâm cặp tiêu chuẩn | $\text{inch}$ | $8$ |
| Áp suất thủy lực vận hành (Rotary Cylinder) | $\text{MPa}$ | $3.5 - 6.0$ |
| Lực kẹp ngàm ước tính tĩnh | $\text{kN}$ | $30 - 40$ |
| Trọng lượng phôi tối đa (Chỉ kẹp hẫng mâm cặp) | $\text{kg}$ | $150$ |
| Trọng lượng phôi tối đa (Có chống tâm ụ động) | $\text{kg}$ | $300$ |
| Đường kính tiện tối đa (Max turning diameter) | $\text{mm}$ | $320$ |
| Chiều dài tiện tối đa (Max turning length) | $\text{mm}$ | $500$ |
| Giới hạn tỷ lệ L/D (Nếu $>3$ BẮT BUỘC dùng ụ động) | - | $3$ |
| Vật liệu Ống kéo (Drawtube) | - | Thép cường lực |
| Cơ cấu chuyển đổi lực (Linear to Radial) | - | Chêm trượt (Wedge Plunger) |
| Môi chất bôi trơn duy trì lực kẹp | - | Mỡ chịu áp lực cao (High-pressure Chuck Grease) |

### 5.3. Đánh dấu giới hạn rủi ro cơ học & Điểm kẹp dập (Pinch Points & Safety Markings)

Kế thừa từ quy định an toàn LOTO ở Chương 1, Bộ phận thiết kế CAD 3D BẮT BUỘC phải trích xuất và thiết lập các nhãn cảnh báo tại cụm Trục chính và Mâm cặp như sau:

*   **Rủi ro kẹp dập cơ học / Nguy cơ nghiền nát (ISO 7010-W024):**
    *   **Vị trí 5:** Không gian kẹp giữa các Ngàm (Jaws) của mâm cặp. Hệ thống áp suất dư ngầm (Trapped pressure) có thể khiến ngàm phóng ra hoặc sập lại bất ngờ khi bảo dưỡng với lực ép $30 - 40\text{ kN}$.
*   **Rủi ro vướng mắc và Cuốn ép (ISO 7010-W025):**
    *   **Vị trí 6:** Vỏ ngoài cửa che cụm mâm cặp chính (Main Chuck Guard) - Nơi tiếp xúc trực tiếp với nguy cơ cuốn áo, tóc hoặc găng tay sợi vào phôi đang gia tốc nhanh lên $4000\text{ RPM}$.
    *   **Vị trí 7:** Nắp che đai truyền động (Drive Belt Cover) của động cơ trục chính.
*   **Rủi ro điện áp cao (ISO 7010-W012):**
    *   **Vị trí 8:** Mặt ngoài nắp bảo vệ Động cơ trục chính (Spindle Motor). Điện áp chết người vẫn tồn tại trên DC Bus trong ít nhất 10 phút sau khi sập cầu dao tổng.
*   **Rủi ro nhiệt độ cao (ISO 7010-W017):**
    *   **Vị trí 9:** Vỏ bọc ngoài thân trục chính và động cơ trục chính. Nhiệt lượng phát sinh từ chu kỳ cắt gọt nặng và ma sát vòng bi có thể đẩy bề mặt này lên trên $70^\circ \text{C}$, gây bỏng nếu chạm tay trần.

---

## 6. Module 3: Hệ thống truyền động Tuyến tính và Đài dao Servo (Linear Drive System & Servo Turret)

Hệ thống truyền động trên CNC-L200 chịu trách nhiệm định vị dao cụ với vận tốc cực lớn đồng thời phải triệt tiêu độ rơ cơ học (Backlash) để đảm bảo dung sai gia công. Khu vực này bao hàm những cơ cấu di chuyển nhanh và ẩn chứa rủi ro đâm sầm (Crash) cao nhất.

### 6.1. Đặc tả kỹ thuật Đài dao Servo (Servo Turret & Curvic Coupling)

Đài dao sử dụng động cơ AC Servo kết hợp hệ thống nhả khớp/khóa khớp bằng áp suất thủy lực nhằm đạt được tốc độ thay dao $0.2\text{ giây}$/trạm. Cơ chế khóa sử dụng khớp nối răng 3 mảnh (Curvic Coupling) cho phép tự định tâm và phân tán lực va đập khi gia công ngắt quãng.

**Bảng 3.1: Thông số kỹ thuật Đài dao Servo**

| Hạng mục thiết kế | Đơn vị | Giá trị / Chuẩn giới hạn |
| :--- | :--- | :--- |
| Loại đài dao điều khiển | - | Động cơ AC Servo |
| Số vị trí trạm dao (Tool Stations) | Trạm | $12$ |
| Kích thước rãnh gá cán dao vuông | $\text{mm}$ | $25 \times 25$ |
| Kích thước lỗ gá cán dao tròn (Boring) | $\text{mm}$ | Tối đa $\varnothing 40$ |
| Thời gian phân độ (Index time) - Trạm kế tiếp | $\text{Giây (s)}$ | $0.2$ |
| Thời gian phân độ (Index time) - Trạm xa nhất | $\text{Giây (s)}$ | $0.6$ |
| Độ chính xác lặp lại (Repeatability) | $\text{mm}$ | $\pm 0.002$ |
| Cơ chế khóa cứng đài dao (Locking Mechanism)| - | Khớp nối răng (Curvic Coupling 3 mảnh) |
| Áp suất thủy lực yêu cầu để Khóa/Nhả khớp | $\text{MPa}$ | $3.5 - 6.0$ |
| Hành trình trượt dọc trục để nhả khớp (Unclamp) | $\text{mm}$ | $\approx 5$ |
| Trọng lượng tĩnh cụm đài dao | $\text{kg}$ | TBD (To Be Determined) |

### 6.2. Đặc tả Hệ thống truyền động tuyến tính (Linear Drive - X/Z Axes)

Hệ thống trục X và Z sử dụng vít me bi siêu chính xác, kết hợp truyền động trực tiếp (Direct drive) qua khớp nối mềm để loại bỏ ma sát trượt và độ rơ. Do cấu trúc băng máy nghiêng $45^\circ$, trục X chịu tác động của trọng lực nên động cơ bắt buộc phải tích hợp phanh từ vĩnh cửu.

**Bảng 3.2: Thông số Truyền động Tuyến tính Trục X / Z**

| Hạng mục thiết kế | Đơn vị | Giá trị / Vật liệu / Chuẩn giới hạn |
| :--- | :--- | :--- |
| Hành trình làm việc Trục X (X-Axis Travel) | $\text{mm}$ | $175$ |
| Hành trình làm việc Trục Z (Z-Axis Travel) | $\text{mm}$ | $520$ |
| Tốc độ di chuyển nhanh tối đa - Trục X | $\text{m/phút}$ | $24$ |
| Tốc độ di chuyển nhanh tối đa - Trục Z | $\text{m/phút}$ | $30$ (Tương đương $500\text{ mm/s}$) |
| Loại thanh ray dẫn hướng (Guideways) | - | Tuyến tính loại con lăn (Roller LM Guideways) |
| Chuẩn cấp độ Vít me bi (Ball screw grade) | - | Cấp siêu chính xác C3 |
| Kích thước Vít me bi (Đường kính x Bước ren) | $\text{mm}$ | $\varnothing 32$, Bước (Pitch) $10$ |
| Phương thức liên kết Động cơ - Vít me | - | Trực tiếp (Direct drive) qua khớp nối mềm |
| Hệ thống Phanh chống rơi (Trục X) | - | Phanh từ vĩnh cửu (Permanent Magnetic Brake) |
| Công suất động cơ Servo (Trục X / Trục Z) | $\text{kW}$ | TBD (To Be Determined) |

### 6.3. Đánh dấu giới hạn rủi ro cơ học & Điểm kẹp dập (Pinch Points)

Khu vực di chuyển của đài dao là nơi giao thoa giữa tốc độ cao ($30\text{ m/phút}$) và lực ép servo khổng lồ. Yêu cầu bộ phận thiết kế 3D dán nhãn rủi ro ở các vị trí tĩnh và trên cụm chuyển động:

*   **Rủi ro kẹp dập cơ học / Nguy cơ nghiền nát (ISO 7010-W024):**
    *   **Vị trí 10:** Hai bên hông của khối đài dao (Turret body). Điểm kẹp dập trực tiếp hình thành giữa đài dao và mâm cặp (khi tiến về -Z) hoặc ụ động (khi tiến về +Z) ở tốc độ cắt gọt và di chuyển nhanh.
    *   **Vị trí 11:** Không gian hở giữa mâm dao quay (Turret disk) và thân ụ dao tĩnh trong quá trình nhả khớp (Unclamp $5\text{mm}$).
*   **Rủi ro Rơi tự do / Bất ngờ sập cơ khí (Drop Hazard):**
    *   **Vị trí 12:** Khu vực ngay bên dưới đài dao trục X. Nếu quy trình bảo dưỡng nhả áp suất thủy lực mà mất điện/Servo mất phanh đột ngột, mâm dao mất cân bằng tĩnh sẽ **rơi tự do (Free-fall / Drop)** chém xuống băng máy. Yêu cầu thiết kế không gian cho phép kỹ thuật viên chèn Khối chặn cơ khí (Mechanical Blocks) trước khi thao tác LOTO.
*   **Cảnh báo Va chạm chết người (Crash Hazard):**
    *   **Vị trí 13:** Cảnh báo liên động cửa (Door Interlock). Tuyệt đối cấm thiết kế cho phép vô hiệu hóa (Bypass) công tắc cửa an toàn. Tốc độ trục Z đạt $500\text{ mm/giây}$ không cho phép con người có thời gian phản xạ lùi lại nếu đứng trong buồng máy.

---

## 7. Module 4: Cụm Ụ động Thủy lực (Tailstock & Hydraulic Quill)

Cụm Ụ động trên CNC-L200 là tổ hợp cơ - thủy lực cực kỳ quan trọng, bắt buộc sử dụng để hỗ trợ gia công khi tiện các trục dài có tỷ lệ Chiều dài/Đường kính ($L/D$) $> 3$, hỗ trợ phôi có trọng lượng lên đến $300\text{ kg}$. Hệ thống được thiết kế linh hoạt với thân ụ động di chuyển trên băng máy và nòng thủy lực độc lập.

### 7.1. Đặc tả kỹ thuật Cơ khí & Thủy lực (Mechanical & Hydraulic Specs)

Cụm ụ động được chia làm hai phần: Thân ụ động (Tailstock Body) khóa chặt xuống băng máy (chốt cơ khí/kẹp thủy lực) và Nòng ụ động (Hydraulic Quill) cung cấp lực đẩy hằng số.

**Bảng 4.1: Thông số kỹ thuật Cụm Ụ động**

| Hạng mục thiết kế | Đơn vị | Giá trị / Vật liệu / Chuẩn giới hạn |
| :--- | :--- | :--- |
| Hành trình thân ụ động (Body Travel) | $\text{mm}$ | $450$ |
| Hành trình nòng ụ động (Quill Stroke) | $\text{mm}$ | $80$ |
| Đường kính nòng ụ động (Quill Diameter) | $\text{mm}$ | $65$ |
| Độ côn mũi tâm (Tailstock Taper) | - | MT4 |
| Chuẩn vòng bi mũi tâm quay (Live Center) | - | Tiếp xúc góc (Angular contact bearings) |
| Áp suất thủy lực vận hành Nòng | $\text{MPa}$ | $3.5 - 6.0$ |
| Lực đẩy nòng tối đa (Tại $3.5 - 6.0\text{ MPa}$) | $\text{kN}$ | $2.5 - 4.5$ |
| Loại van an toàn chống rớt nòng | - | Van một chiều chống lún (Pilot-operated check valve) |
| Vật liệu thân Ụ động | - | TBD (To Be Determined) |
| Vật liệu Nòng Ụ động (Quill) | - | TBD (To Be Determined) |
| Khoảng cách gá đặt an toàn (Mũi tâm tới phôi trước khi kích nòng) | $\text{mm}$ | $30 - 50$ |

### 7.2. Động lực học Chống tâm bù nhiệt (Thermal Compensation Dynamics)

Trong quá trình tiện phá thô, phôi thép dài hấp thụ nhiệt lượng lớn (lên tới $800^\circ\text{C}$ tại vùng cắt) và bắt đầu giãn nở tuyến tính (Linear Thermal Expansion) dọc theo trục Z. Thiết kế xylanh thủy lực điều khiển nòng Quill của CNC-L200 đóng vai trò như một "lò xo hằng số". 
Khi phôi giãn nở và sinh ra lực dọc trục (Axial thrust) đẩy ngược lại mũi tâm, áp suất thủy lực điều tiết sẽ cho phép nòng Quill lùi lại siêu vi mô, duy trì lực ép tĩnh từ $2.5 - 4.5\text{ kN}$ thay vì tăng vọt. Cơ chế tự tự động bù trừ này loại bỏ hoàn toàn nguy cơ phôi bị uốn cong (võng phôi) hoặc vỡ cụm vòng bi tiếp xúc góc của mũi tâm quay (Live Center).

### 7.3. Đánh dấu giới hạn rủi ro cơ học & Điểm kẹp dập (Safety Markings)

Nhóm CAD 3D BẮT BUỘC chỉ định nhãn dán an toàn cho khu vực Ụ động nhằm cảnh báo nguy cơ kẹp dập và thảm họa áp suất bẫy:

*   **Rủi ro kẹp dập cơ học / Nguy cơ nghiền nát (ISO 7010-W024):**
    *   **Vị trí 14:** Khu vực tiếp xúc giữa Mũi tâm (Live Center) và lỗ tâm của phôi. Khi đạp công tắc chân (Foot Switch), nòng lao ra ép vào với lực tĩnh có thể đạt $4.5\text{ kN}$, đủ sức nghiền nát ngón tay nếu không rút tay kịp khỏi phôi liệu.
*   **Rủi ro Áp suất bẫy (Trapped Pressure / High Pressure Fluid):**
    *   **Vị trí 15:** Cụm van một chiều chống lún (Pilot-operated check valves) và các tuy-ô thủy lực kết nối với thân xylanh nòng ụ động. Van này giam lỏng áp suất lên tới $6.0\text{ MPa}$ kể cả khi máy đang tắt nguồn nhằm chống rớt nòng. Nếu nới lỏng ốc vít bảo dưỡng mà chưa sử dụng chốt xả cơ khí dự phòng (Manual Override), nòng nén sẽ phóng ra như đạn pháo hoặc tia dầu cắt đứt chi thể.
*   **Cảnh báo Va chạm (Crash Hazard):**
    *   **Vị trí 16:** Toàn bộ khu vực di chuyển dọc băng máy của thân ụ động. Trong quy trình đưa máy về gốc (Zero Return), nếu lùi trục Z (+Z) trước khi nâng trục X (+X) lên cao, đài dao servo sẽ quét ngang và đâm sầm (crash) vào thân ụ động.

---

## 8. Module 5: Hệ thống Cách ly Năng lượng An toàn (LOTO - Lockout/Tagout)

Hệ thống LOTO (Lockout/Tagout) là quy trình an toàn bắt buộc, nhằm triệt tiêu hoàn toàn các nguồn năng lượng tiềm năng (Zero Energy State - ZES) trước khi nhân viên kỹ thuật tiến hành bảo dưỡng, sửa chữa hoặc can thiệp vào bên trong vùng nguy hiểm của máy CNC-L200. Thiết kế của máy phải tích hợp sẵn các cơ cấu khóa vật lý và van xả áp tại các điểm LOTO trọng yếu để người vận hành dễ dàng thao tác.

### 8.1. Phân loại và Đặc tả các điểm LOTO (Isolation Points)

Bộ phận thiết kế cơ điện (MEP) và Thủy lực/Khí nén chịu trách nhiệm bố trí các điểm cách ly năng lượng tại vị trí dễ tiếp cận, tránh các không gian hẹp (Confined space). Tất cả các van/công tắc cách ly phải có thiết kế lỗ móc khóa (Padlock holes) tiêu chuẩn tối thiểu $\varnothing 8\text{mm}$.

**Bảng 5.1: Danh sách các điểm Cách ly Năng lượng (LOTO Points)**

| Mã LOTO | Nguồn năng lượng | Vị trí / Thiết bị cách ly trên máy | Cảnh báo & Quy trình triệt tiêu năng lượng ngầm (Stored Energy) |
| :--- | :--- | :--- | :--- |
| **LOTO-E1** | Điện lưới (380VAC) | Cầu dao xoay tổng (Main Disconnect Switch) đặt ngoài Tủ điện chính. | Gạt về OFF và móc khóa. **Tuyệt đối không mở tủ điện ngay lập tức** sau khi khóa. |
| **LOTO-E2** | Điện áp ngầm (DC Bus) | Tụ điện lưu trữ bên trong Servo / Spindle Amplifier. | **NGUY HIỂM CHẾT NGƯỜI:** Chờ ít nhất 15 phút sau khi khóa LOTO-E1 để điện áp DC Bus xả dưới ngưỡng an toàn ($50\text{VDC}$). Bắt buộc đo kiểm bằng VOM trước khi chạm vào bo mạch. |
| **LOTO-H1** | Thủy lực động (Hydraulic) | Cụm động cơ Bơm thủy lực (Hydraulic Pump Unit). | Ngắt nguồn điện động cơ bơm (Đã bao hàm trong thao tác LOTO-E1). |
| **LOTO-H2** | Áp suất bẫy (Trapped Pressure) | Van xả áp (Bleed Valve) tại các cụm mâm cặp, đài dao và ụ động. | Mở van xả áp cơ khí bằng tay để đưa áp suất bẫy (có thể đạt $6.0\text{ MPa}$) trong đường ống và xylanh về $0\text{ MPa}$. Quan sát đồng hồ áp suất để xác nhận. |
| **LOTO-P1** | Khí nén động (Pneumatic) | Van khóa khí nén đầu vào (Air Supply Isolation Valve) tại cụm FRL. | Gạt van khóa về vị trí xả (Exhaust). Khí nén tồn dư trong ống dẫn phải được xả ra môi trường (kèm tiếng "xì" đặc trưng). Móc khóa vào van. |
| **LOTO-M1** | Cơ năng / Trọng lực (Gravity) | Trục nghiêng X và Đài dao Servo (Servo Turret). | Đưa trục X về vị trí dưới cùng hoặc vị trí an toàn. **Bắt buộc** chèn khối chặn cơ khí (Mechanical Blocking) chống sập đài dao trước khi ngắt phanh điện từ. |

### 8.2. Quy trình thiết lập Trạng thái Không Năng lượng (Zero Energy State - ZES)

Thiết kế tài liệu Hướng dẫn sử dụng (User Manual) và nhãn dán quy trình trên thân máy CNC-L200 phải tuân thủ nghiêm ngặt chuỗi thao tác LOTO 6 bước chuẩn công nghiệp (OSHA):

1.  **Chuẩn bị (Prepare):** Nhận diện toàn bộ 4 nguồn năng lượng (Điện, Thủy lực, Khí nén, Cơ năng) trên máy CNC-L200 theo sơ đồ tại mục 8.1.
2.  **Tắt máy (Shutdown):** Dừng máy theo chu trình bình thường (Bấm Cycle Stop -> Spindle Stop -> Đưa máy về Home -> Tắt màn hình điều khiển CNC).
3.  **Cách ly (Isolate):** Kích hoạt các điểm cách ly năng lượng vật lý bao gồm **LOTO-E1** (Cầu dao tổng) và **LOTO-P1** (Van khí nén).
4.  **Khóa và Treo thẻ (Lock & Tag):** Kỹ thuật viên bảo dưỡng trực tiếp bấm ổ khóa cá nhân (Padlock) màu đỏ và treo thẻ cảnh báo (Tagout) ghi rõ Tên, Số điện thoại, Ngày tháng vào các điểm vừa cách ly.
5.  **Giải phóng năng lượng ngầm (Stored Energy Release):** 
    *   Chờ 15 phút cho **LOTO-E2** xả hết điện năng trong tụ. 
    *   Thao tác xả các van áp suất bẫy **LOTO-H2**. 
    *   Lắp đặt và siết ốc các khối chặn cơ khí **LOTO-M1** để giữ trục X.
6.  **Xác nhận (Verify):** Bấm nút khởi động máy (Cycle Start) hoặc kiểm tra lại bằng đồng hồ vạn năng (VOM) / Đồng hồ áp suất để chắc chắn máy hoàn toàn không thể hoạt động và không còn năng lượng. Trả các nút bấm về vị trí ban đầu sau khi xác nhận.