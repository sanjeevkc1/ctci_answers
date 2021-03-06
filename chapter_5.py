                                                    # CTCI Bit Manipulations

# 1. insert 'm' into 'n' starting from j ending in i
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

    @staticmethod
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

# 2. convert a floating number
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

# 3. Return longest sub sequence of ones
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

# 4. print the immediate smallest and largest
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

    # brute-force
    def get_next_smallest(self):
        temp = self.n
        if(temp > 0):
            ones = self.countSetBits(self.n)
            temp = self.n - 1
            while(ones != self.countSetBits(temp)):
                temp -= 1
        return temp

    # brute-force
    def get_next_largest(self):
        temp = self.n
        if(temp > 0):
            ones = self.countSetBits(self.n)
            temp = self.n + 1
            while(ones != self.countSetBits(temp)):
                temp += 1
        return temp

    #optimized solutions
    def get_prev_smallest_opt(self):
        # get first zero that
        # has 1 to its left side
        import math
        temp = self.n
        if(temp > 0):
            num_of_bits = int(math.log(temp,2)) + 1
            if (((1 << num_of_bits) - temp != 1)): #if the number doesn't have all ones
                # observe the first pair of 0 and 1 where 1 appears before 0
                # For example in 1000010 --> interchange first 0 with 1 and 1 with 0
                l_s_b = 0 if (temp % 2) == 0 else 1
                s_b  = 0 if ((temp >> 1) % 2) == 0 else 1
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
                # once the above step is finished,
                # update zeros with ones and ones and zeros that are to the right side of
                # index variable.
                # eg:     110011
                # output: 101110
                if (one_index > -1 and zero_index > -1):
                    zero_index += one_index + 1
                    while (one_index >= 0):
                        temp = ctci_p1.update_bit(temp,zero_index)
                        temp = ctci_p1.reset_bit(temp,one_index)
                        one_index -= 1
                        zero_index -= 1
        return temp

    def get_next_largest_opt(self):
        # get first zero that
        # has 1 to its left side
        import math
        temp = self.n
        if(temp > 0):
            num_of_bits = int(math.log(temp,2)) + 1
            if ((1 << num_of_bits) - temp != 1): #if the number doesn't have all ones
                # observe the first pair of 0 and 1 where 0 appears before 1
                # For example in 1000010 --> interchange first 1 with 0 and 0 with 1
                # then 1000010 --> 1000100
                l_s_b = 0 if (temp % 2) == 0 else 1
                s_b  = 0 if ((temp >> 1) % 2) == 0 else 1
                one_index = -1
                zero_index = -1
                index = 1
                temp >>= 2
                while (not (not s_b and l_s_b) and temp > 0):
                    if(l_s_b):
                        one_index += 1
                    else:
                        zero_index += 1
                    l_s_b = s_b
                    s_b = 0 if (temp % 2 == 0) else 1
                    temp >>= 1
                    index += 1
                temp = self.n
                temp = ctci_p1.reset_bit(temp,index - 1)
                temp = ctci_p1.update_bit(temp,index)
                # once the above step is finished,
                # update zeros with ones and ones and zeros that are to the right side of
                # index variable.
                # eg:     110011
                # output: 1101110
                if (one_index > -1 and zero_index > -1):
                    one_index += zero_index + 1
                    while (zero_index >= 0):
                        temp = ctci_p1.update_bit(temp,one_index)
                        temp = ctci_p1.reset_bit(temp,zero_index)
                        one_index -= 1
                        zero_index -= 1
            else:
                temp = (temp * 2) + 1
                temp = ctci_p1.reset_bit(temp,num_of_bits - 1)
        return temp

# 5. what is (n & (n -1)) == 0 true and false?
# sol: If n is a power of two or 0, the above expression is true else false.

# 6. Determine how many bits needs to be flipped to convert
#  integer A to B
class ctci_p6(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.count = 0
    def hamming_distance(self):
        a = self.a
        b = self.b
        while (a > 0 and b > 0):
            lsb_a = 0 if (a % 2  == 0) else 1
            lsb_b = 0 if (b % 2 == 0) else 1
            self.count += lsb_a ^ lsb_b
            a >>= 1
            b >>= 1
        while(a > 0):
            self.count += 1
            a >>= 1
        while(b > 0):
            self.count += 1
            b >>= 1
        return self.count

# 7. Swap odd and even bits as few instructions as possible.
# bit0 and bit1 are swapped. bit2 and bit3 are swapped.
class ctci_p7(object):
    def pair_swap(self,a):
        temp = a
        # The idea is first to use even and odd mask variables
        # to get even and odd bits respectively.
        even_mask = 0xAAAAAAAA # In binary it has 32 bits and is equivalent to 101010.......10
        odd_mask = 0x55555555 # In binary it has 32 bits and is equivalent to  010101.......01

        # using these masks we gather only even and odd bits from temp by doing a logical and with temp
        even_mask &= temp
        odd_mask &= temp

        #Now we right shift even_mask and left shift odd_mask by 1
        even_mask >>= 1
        odd_mask <<= 1

        #Finally return the logical or of even and odd mask
        return (even_mask | odd_mask)
      
# 8.Draw line on a screen
class ctci_p8(object):
    # pixels is number of pixels (int)
    # width = width of screen
    # x1, x2, y = Bit number in each pixel on screen starting from most significant bit.
    # Representation: Each pixel is a byte.
    # so if width is 3 then we have 3 * 8 = 24 bits in the row.
    # A pixel can have any value between 0 to 255
    # x1, x2 are one-indexed
    # y is zero-indexed

    def draw_line (self, pixels, width, x1, x2, y):
        height = pixels / width #height of the screen
        if ((x1 > width * 8) or (x2 > width * 8) or (y > height)):
            print "Bad input"
            return None
        if (x1 > x2):
            x1,x2 = x2,x1

        pixels = [0] * (pixels) #initiate pixel array
        mask = 256
        while (x1 <= x2):
            # The current pixel is equal to 'width * height' which gives the row number
            # and add to it the integer division of x1 / 8 which gives column number
            curr_pixel = (width * y) + (x1 - 1) / 8

            # once we have the pixel coords, logical OR with 256 to update
            # the bit with 1. Bit count is kept track through 'x1 - (8 * (curr_pixel % width))'
            pixels [curr_pixel] |= mask >> (x1 - (8 * (curr_pixel % width)))
            x1 += 1
        return pixels



