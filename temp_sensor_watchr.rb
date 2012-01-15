watch( 'lib/.*\.c' )  {|md| commit_and_test}
watch( 'lib/.*\.h' )  {|md| commit_and_test}
watch( '.*\.py' )  {|md| commit_and_test}
watch( '.*\.rb' )  {|md| commit_and_test}

def commit_and_test()
  system("clear")
  current_time = Time.now().to_s
  puts current_time
  puts

  patch_name = current_time.to_s
  patch_name = patch_name.sub(":","-")
  patch_name = patch_name.sub(":","-")
  patch_name = patch_name.sub(" ","-")
  patch_name = patch_name[0..-7]
  patch_name = patch_name
  patch_dir  = "patch/"

  # commit changes to save repo
  system("git add . && git add -u && git commit -m\"" + patch_name + "\"")
  #  system("git format-patch -3 -o" + patch_dir + " HEAD~1 ")
  remote_sha = ""
  File.open("patch/remote_sha","r") do |f|
    remote_sha = f.readline()
    puts "remote_sha is #{remote_sha}"
  end
  begin
    File.delete("bundle/bundle.bundle")
  rescue
  end
#  system("git bundle create bundle/bundle.bundle master ^#{remote_sha}")
  system("git bundle create bundle/bundle.bundle --all")
  system("git log -1  --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative")
#  system("python lib/client.py #{patch_dir}0001-#{patch_name}.patch")
  system("python lib/client.py")
end
