palindrome = 0

def isPalindrome(str)
  half1 = str[0, str.length / 2].reverse
  half2 = str[str.length / 2, str.length].reverse
  return "#{half2}#{half1}" == str
end

for num1 in (1..999).to_a
  for num2 in (1..999).to_a
    result = num1 * num2
    if isPalindrome(result.to_s) && result > palindrome then
      palindrome = result
    end
  end
end

puts palindrome
