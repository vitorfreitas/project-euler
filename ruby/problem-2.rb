class Challenge
  attr_reader :sum

  def initialize
    @sum = 0
  end

  def fib(limit, cur, last)
    if cur >= limit then
      return last
    end
    if cur % 2 == 0 then
      @sum += cur
    end
    return fib(limit, cur + last, cur)
  end
end

c = Challenge.new
c.fib(4_000_000, 2, 1)

puts c.sum
