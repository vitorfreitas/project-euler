count = 0
whileContinue = true
value = 1

while value == 1
  testPassed = false
  count += 20

  for div in (1..20).to_a
    if count % div != 0 then
      break
    end
    if div == 20 then
      testPassed = true
    end
  end

  if testPassed then
    value = count
  end
end

puts value
