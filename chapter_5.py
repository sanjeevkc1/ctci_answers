                                                    # CTCI Bit Manipulations

# ____________________
# insert 'm' into 'n' starting from j ending in i
# j - i = # of bits in m
class ctci_p1(object):

    @staticmethod
    #reset i'th bit in n with 0
    def reset_bit(n,i):
        mask = ~(1 << i)
        return (n & mask)

    @staticmethod
    #update i'th bit in n with 1
    def update_bit(n,i):
        # mask = (1 << i) & 0xFFFFFFFF
        mask = (1 << i)
        return (n | mask)

    def replace_num(self,m,n,i,j):
        while(i <= j):
            last_bit = 0 if(m % 2 == 0) else 1
            if(last_bit):
                n = self.update_bit(n,i)
            else:
                n = self.reset_bit(n,i)
            m >>= 1
            i += 1
        return n

# ____________________
# convert a floating number
# to binary. return the binary
# as string
class ctci_p2(object):

    def fraction_to_decimal(self,n):
        result = ''
        temp = n
        while(temp != 1.0):
            temp = (temp - int(temp)) * 2
            result += str(int(temp))
        return result

# ____________________
# Return longest sub sequence of ones
# by replacing at most one zero
# input    1775 (11011101111)
# Output   8    (110[11111111])

class ctci_p3(object):

    def longest_ones_sequence(self,n):
        first_zero = False
        init_one = False
        curr_len = 0
        main_len = 0
        temp = n
        if(temp == 0):
            return 1
        elif ((temp == 1) or ((n & (n - 1)) == 0)):
            return 2
        else:
            while(temp > 0):
                last_bit = 0 if (temp % 2 == 0) else 1
                if(last_bit):
                    curr_len += 1
                    if(not init_one):
                        init_one = True
                else:
                    if (init_one):
                        if (not first_zero):
                            first_zero = True
                            curr_len += 1
                        else:
                            main_len = max(curr_len,main_len)
                            curr_len = 0
                            first_zero = False
                temp >>= 1
            return main_len

# ____________________
# print the immediate smallest and largest
# number of the given number that has same
# number of  1s

class ctci_p4(object):

    # brute force solution
    def __init__(self,n):
        self.n = n

    def countSetBits(self,n):
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count

    def get_next_smallest(self):
        ones = self.countSetBits(self.n)
        temp = self.n - 1
        while(ones != self.countSetBits(temp)):
            temp -= 1
        return temp

    def get_next_biggest(self):
        ones = self.countSetBits(self.n)
        temp = self.n + 1
        while(ones != self.countSetBits(temp)):
            temp += 1
        return temp

    #optimized solution
    def get_next_smallest_optimized(self):
        # get first zero that
        # has 1 to its left side
        import math
        temp = self.n
        num_of_bits = int(math.log(temp,2)) + 2

        if ((1 << num_of_bits) - temp == 1):
            print "Init:  ", bin(self.n)
            l_s_b = 0 if (temp % 2) == 0 else 1
            s_b  = 0 if (temp % 2) == 0 else 1
            one_index = -1
            zero_index = -1
            index = 1
            temp >>= 2

            while (not (s_b and not l_s_b) and temp > 0):
                if(l_s_b):
                    one_index += 1
                else:
                    zero_index += 1

                l_s_b = s_b
                s_b = 0 if (temp % 2 == 0) else 1
                temp >>= 1
                index += 1

            temp = self.n
            temp = ctci_p1.update_bit(temp,index - 1)
            temp = ctci_p1.reset_bit(temp,index)

            if (one_index > -1 and zero_index > -1):
                zero_index += one_index + 1
                while (one_index >= 0):
                    temp = ctci_p1.update_bit(temp,zero_index)
                    temp = ctci_p1.reset_bit(temp,one_index)
                    one_index -= 1
                    zero_index -= 1
            print "result:", bin(temp)
        else:
            import math
            a = temp
            b = temp << 1
            b = ctci_p1.update_bit(b,0)
            b = ctci_p1.reset_bit(b,int(math.log(b,2)) - 1)
            print [a,b]

# s = ctci_p4(25)
# s.get_next_smallest_optimized()
#
# s = ctci_p4(49)
# s.get_next_smallest_optimized()
#
# s = ctci_p4(99)
# s.get_next_smallest_optimized()

s = ctci_p4(5)
s.get_next_smallest_optimized()