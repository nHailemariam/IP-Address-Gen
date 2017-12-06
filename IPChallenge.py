class IpGenerate(object):
    def __init__(self, numbers):
        self.str_input = numbers
        self.IPs = []
        if ( self.check(self.str_input)):
            self.IPs = self.generate(self.str_input)

    def check(self, num):
        success = True
        try:
            if num == "" or num < 0 or len(num) < 4 or len(num) > 12:
                success = False
            num = int(num)


        except ValueError:
            success = False

        if (success == False):
            print "IP can't be composed of letters or negative integer \nlength of Input must be greater than 3 and less than 13"
        return success

    def merge(self, left, right, store):
        merged = ""

        for i in range(len(left)):
            merged += left[i]
            if merged not in store:
                store.append(merged)

        for i in range(len(right)):
            merged += right[i]
            if merged not in store:
                store.append(merged)

        return merged

    def divide(self, part_nums, store):
        if len(part_nums) < 2:
            return part_nums
        else:
            middle = len(part_nums)//2
            left = self.divide(part_nums[:middle], store)
            right = self.divide(part_nums[middle:], store)
            return self.merge(left, right, store)

    def split(self, nums, store):
        for i in range(len(nums)):
            self.divide(nums[i:i+3], store)
        if nums[-1] not in store:
            store.append(nums[-1])
        return store

    def generate(self, input):
        sent = []
        sliced = self.split(input, sent)
        IP = ""
        possible_IP = []
        for i in sliced:
            for j in sliced:
                for k in sliced:
                    for l in sliced:

                        if int(i) > 255 or int(j) > 255 or int(k) > 255 or int(l) > 255:
                            continue
                        IP = i + "." + j + "." + k + "." + l
                        if IP.replace(".", "") == input:
                            possible_IP.append(IP)

        return possible_IP

    def printIPs(self):
        print str(self.IPs)



input = raw_input("Enter an integer: ")
ips = IpGenerate(input)
print "possible ip ", ips.IPs

