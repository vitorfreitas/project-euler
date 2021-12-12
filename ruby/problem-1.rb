range = (1..1000).to_a
sum = 0

for num in range do
  if num % 3 == 0 || num % 5 == 0 then
    sum += num
  end
end

puts sum
