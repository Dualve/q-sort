def start_sort(arr):
	quick_sort(arr, 0, len(arr)-1)
	
def quick_sort(arr, low, hight):
	if hight-low < len(arr)-1 and low < hight:
		quick_selection(arr, low, hight)
	elif low < hight:
		p = divide(arr, low, hight)
		quick_sort(arr, low, p - 1)
		quick_sort(arr, p + 1, hight)
	
	
def divide(arr, low, hight):
	markerIndex = get_marker(arr, low, hight)
	markerValue = arr[markerIndex]
	arr[markerIndex], arr[low] = arr[low], arr[markerIndex]
	border = low

	for i in range(low, hight+1):
		if arr[i] < markerValue:
			border += 1
			arr[i], arr[border] = arr[border], arr[i]
	arr[low], arr[border] = arr[border], arr[low]
	return (border)

def get_marker(arr, low, hight):
	mid = (hight + low) // 2
	s = sorted([arr[low], arr[mid], arr[hight]])
	if s[1] == arr[low]:
		return low
	elif s[1] == arr[mid]:
		return mid
	return hight

	
def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]



arr = [5,9,-12,1,2,4,8,6,200,3,7,10,12,-1,19,13,14,11,17,16,18,20,110,-12,123]
print(arr)
start_sort(arr)
print(arr)
