import re
import json

def parse_procedure_algorithm(text: str) -> str:
    # 1. Định nghĩa Regex và Từ điển (Rules)
    # Tách văn bản theo từ khóa "Bước X:"
    step_pattern = re.compile(r'(Bước\s+\d+:?)(.*?)(?=Bước\s+\d+:?|$)', re.IGNORECASE | re.DOTALL)
    
    # Biểu thức chính quy tìm thông số kỹ thuật (Số + Đơn vị)
    param_pattern = re.compile(r'\d+(?:[.,]\d+)?\s*(?:bar|độ C|V|A|kg|m|cm|mm|rpm)')
    
    # Từ điển tra cứu cứng (Có thể thay bằng mô hình POS Tagging của underthesea/spaCy để linh hoạt hơn)
    warning_keywords = ["không", "cấm", "chú ý", "cảnh báo", "nguy hiểm", "tránh"]
    tool_keywords = ["kính thăm", "công tắc", "nút", "đồng hồ", "van", "cờ lê", "màn hình"]
    
    schema_result = {
        "procedure_name": "Quy trình vận hành máy móc",
        "total_steps": 0,
        "steps": []
    }
    
    # 2. Xử lý thuật toán
    steps = step_pattern.findall(text)
    schema_result["total_steps"] = len(steps)
    
    for step_idx, (step_prefix, step_content) in enumerate(steps, 1):
        content = step_content.strip()
        sentences = [s.strip() for s in content.split('.') if s.strip()]
        
        # Trích xuất thông số
        params = param_pattern.findall(content)
        
        # Phân loại câu: Cảnh báo vs Hành động
        warnings = []
        actions = []
        for sentence in sentences:
            is_warning = any(kw in sentence.lower() for kw in warning_keywords)
            if is_warning:
                warnings.append(sentence)
            else:
                actions.append(sentence)
                
        # Trích xuất công cụ từ nội dung bước
        tools = [tool for tool in tool_keywords if tool in content.lower()]
        
        # 3. Đóng gói vào Schema
        schema_result["steps"].append({
            "step_number": step_idx,
            "action": ". ".join(actions) if actions else content,
            "parameters": params if params else None,
            "tools_required": list(set(tools)),
            "safety_warning": ". ".join(warnings) if warnings else None
        })
        
    return json.dumps(schema_result, ensure_ascii=False, indent=2)

# --- Chạy thử nghiệm ---
sample_text = """
Hướng dẫn khởi động máy nén khí trục vít:
Bước 1: Kiểm tra mức dầu bôi trơn qua kính thăm. Đảm bảo mức dầu nằm giữa vạch xanh. Không dùng tay không chạm vào van xả.
Bước 2: Bật công tắc nguồn điện chính. 
Bước 3: Nhấn nút ON trên bảng điều khiển. Quan sát áp suất trên đồng hồ, chờ đến khi đạt 7 bar thì máy tự động chạy. Chú ý áp suất không vượt quá 10 bar.
"""

result = parse_procedure_algorithm(sample_text)
print(result)