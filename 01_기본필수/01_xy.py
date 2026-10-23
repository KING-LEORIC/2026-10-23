"""01 기본필수: CSV에서 입력과 정답을 각각 꺼냅니다."""
from pathlib import Path
import pandas as pd

# 제공: 이 Python 파일과 같은 폴더에 있는 CSV를 읽습니다. 작업 폴더를 바꾸어도 됩니다.
HERE = Path(__file__).resolve().parent
data = pd.read_csv(HERE / "requests.csv")

# X는 예측 전에 알 수 있는 정보입니다. ID와 정답은 입력에 넣지 않습니다.
# 입력 열에 input_chars와 task_type를 넣습니다.
X = data[["input_chars", "task_type"]].copy()
# 정답 열에 failed를 선택합니다. 0은 성공, 1은 실패입니다.
y = data["failed"].copy()

print("입력 열:", X.columns.tolist())
print("X 모양:", X.shape)
print("y 모양:", y.shape)
print("처음 3개 정답:", y.head(3).tolist())
