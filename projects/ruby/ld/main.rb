# Override the String class to add a colorize method
class String
    def colourise(color_code)
        "\e[#{color_code}m#{self}\e[0m"
    end
end

# Main function
def main
    directory = ARGV[0] || "."

    begin
        # Sort the entries by directory first, then alphabetically
        entries = Dir.entries(directory).sort_by do |entry|
            # Sort directories first
            if File.directory?(File.join(directory, entry))
                "0#{entry}"
            else
                "1#{entry}"
            end
        end

        # Print the header
        puts "Type | Permissions | Owner | Group | Size   | Name"

        # Print the entries
        entries.each do |entry|
            if entry == "." || entry == ".."
                next
            end

            # Get the full path of the entry
            path = File.join(directory, entry)

            # Get the file type
            type = File.directory?(path) ? "d" : "-"

            # Get the permissions
            permissions = File.stat(path).mode.to_s(8)[-3..-1]

            # Get the owner
            owner = File.stat(path).uid

            # Get the group
            group = File.stat(path).gid

            # Get the size
            size = File.stat(path).size

            # Convert the size to human readable format
            if size >= 1024 * 1024 * 1024
                size = "#{(size / (1024 * 1024 * 1024)).round(2)}GB"
            elsif size >= 1024 * 1024
                size = "#{(size / (1024 * 1024)).round(2)}MB"
            elsif size >= 1024
                size = "#{(size / 1024).round(2)}KB"
            else
                size = "#{size}B"
            end

            # Create the output string
            output = "#{type.ljust(6).colourise(36)} #{permissions.ljust(12)}  #{owner.to_s.ljust(6)}  #{group.to_s.ljust(6)}  #{size.rjust(6)}   "

            # Check if the entry is a directory
            if File.directory?(path)
                # Colourise the output string
                output += entry.colourise(34)
            else
                output += entry.colourise(35)
            end

            # Print the output string
            puts output
        end
    rescue Exception => e
        puts e.message
    end
end

if __FILE__ == $0
    main
end
