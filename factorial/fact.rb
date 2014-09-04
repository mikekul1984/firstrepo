#! /usr/bin/env ruby
def factorial(n)
	if n == 0
		1
	else
		n * factorial(n-1)
	end
end

0.upto(16) do |n|
	print(n, "! = ", factorial(n), "\n")
end
