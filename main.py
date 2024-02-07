class Solution:
    def frequencySort(self, s: str) -> str:
        s_counter = Counter(s)
        sorted_s = ''
        # # Sort the Counter by value (frequency) in descending order , item[0] means the key and item[1] is the value
        # sorted_counter = sorted(s_counter.items(),key = lambda item: item[1], reverse=True)
            
        # # Reconstruct the list of characters, repeating each character by its count
        # sorted_s = [char * count for char,count in sorted_counter]

        # return ''.join(sorted_s)

        for char, count in s_counter.most_common():
            sorted_s += char*count


        return sorted_s
