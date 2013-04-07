VERSION = File.open('VERSION').gets.strip

def colorize(text, color)
  color_codes = {
    :black    => 30,
    :red      => 31,
    :green    => 32,
    :yellow   => 33,
    :blue     => 34,
    :magenta  => 35,
    :cyan     => 36,
    :white    => 37
  }
  code = color_codes[color]
  if code == nil
    text
  else
    "\033[#{code}m#{text}\033[0m"
  end
end

def virtual_env(command, env="env33")
  sh "source #{env}/bin/activate ; #{command}"
end

def create_virtual_env(dir, python)
  sh "virtualenv #{dir} -p #{python}"
  virtual_env("pip install -r requirements.txt")
  virtual_env("pip install -r requirements-test.txt")
end

task :clean => [] do
  sh "rm -rf ~*"
  sh "rm -rf *.pyc *.pyo"
  sh "rm -rf data/"
  sh "rm -rf *.egg-info"
  sh "rm -rf dist/"
end

task :install => [] do
  sh "python --version"
  sh "ruby --version"
  sh "easy_install pip"
end

task :dev_env => [] do
  create_virtual_env("env26", "python2.6")
  create_virtual_env("env27", "python2.7")
  create_virtual_env("env32", "python3.2")
  create_virtual_env("env33", "python3.3")
end

task :tests => [] do
  virtual_env("nosetests", "env26")
  virtual_env("nosetests", "env27")
  virtual_env("nosetests", "env32")
  virtual_env("nosetests", "env33")
end

task :tag => [:tests] do
  sh "git tag #{VERSION}"
  sh "git push origin #{VERSION}"
end

task :reset_tag => [] do
  sh "git tag -d #{VERSION}"
  sh "git push origin :refs/tags/#{VERSION}"
  sh "git tag #{VERSION}"
  sh "git push origin #{VERSION}"
end

task :publish => [:tests, :tag] do
  # http://guide.python-distribute.org/quickstart.html
  # python setup.py sdist
  # python setup.py register
  # python setup.py sdist upload
  # Manual upload to PypI
  # http://pypi.python.org/pypi/THE-PROJECT
  # Go to 'edit' link
  # Update version and save
  # Go to 'files' link and upload the file
  virtual_env("python setup.py sdist upload")
end

task :default => [:server]

