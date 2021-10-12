class DeletableClass:
	def __del__(self):
		print("delete")

d = DeletableClass()
del d

## __init__와 대비되는 용도
## 객체가 삭제되기 전에 처리해야 할 마무리 행동 정의