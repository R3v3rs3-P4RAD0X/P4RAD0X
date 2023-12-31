def read_file(name)
  file = File.open(name, "r")
  lines = file.readlines
  env = {}
  for line in lines
    key, val = line.split("=")
    env[key] = val
  end
  file.close
  env
end

require "discordrb"

def main
  env = read_file ".env"

  bot = Discordrb::Bot.new token: env["DISCORD_BOT_TOKEN"]

  bot.ready do |event|
    puts "Logged in as #{bot.profile.username} (ID:#{bot.profile.id})"
  end

  bot.message do |event|
    if event.content.start_with? "!"
      content = event.content.slice!(0)
      content = content.strip!
      content = content.split(" ")

      command, *args = content

      if command == "ping"
        event.respond "Pong!"
      end
    end
  end

  bot.run
end

if __FILE__ == $0
  main
end
