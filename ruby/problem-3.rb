class Challenge
  def isDivisable(num1, num2)
    return num1 % num2 == 0
  end

  def isPrime(num)
    if num >= 1 && num <= 3 then
      return TRUE
    end
    return Math.sqrt(num) * Math.sqrt(num) == num
  end

  def main(value)
    primes = []
    for num in (3...Math.sqrt(value).round()).to_a
      if self.isDivisable(value, num) && self.isPrime(num) then
        primes.push(num)
      end
    end
    return primes
  end
end

c = Challenge.new
puts c.main(600851475143)
# puts c.isPrime(13)
