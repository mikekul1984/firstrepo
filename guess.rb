words = ['a', 'b', 'c']
secret = words[rand(3)]

print "guess? "
while guess = STDIN.gets
	guess.chop!
	if guess == secret
		print "You win!\n"
		break
	else
		print "Wrong\n"
	end
	print "guess? "
end
print "The word was ", secret, ".\n"
