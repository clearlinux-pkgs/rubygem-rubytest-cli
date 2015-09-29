#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rubytest-cli
Version  : 0.2.0
Release  : 3
URL      : https://rubygems.org/downloads/rubytest-cli-0.2.0.gem
Source0  : https://rubygems.org/downloads/rubytest-cli-0.2.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: rubygem-rubytest-cli-bin
BuildRequires : ruby
BuildRequires : rubygem-ansi
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rubytest

%description
# Ruby Test CLI
Command line interface for running tests for RubyTest-based
test frameworks.

%package bin
Summary: bin components for the rubygem-rubytest-cli package.
Group: Binaries

%description bin
bin components for the rubygem-rubytest-cli package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rubytest-cli-0.2.0
gem spec %{SOURCE0} -l --ruby > rubygem-rubytest-cli.gemspec

%build
gem build rubygem-rubytest-cli.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rubytest-cli-0.2.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/rubytest-cli-0.2.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/autopath%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/autopath%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/cdesc-CLI.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/chdir%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/chdir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/config_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/format%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/load_config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/loadpath-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/makelist-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/profile%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/profile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/require_dotopts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/requires-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/run-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/units-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/verbose%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/CLI/verbose%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/Test/cdesc-Test.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/page-HISTORY_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/page-LICENSE_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/rubytest-cli-0.2.0/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/.index
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/HISTORY.md
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/README.md
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/bin/ruby-test
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/bin/rubytest
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/lib/rubytest-cli.rb
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/lib/rubytest-cli.yml
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/man/rubytest.1
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/man/rubytest.1.html
/usr/lib64/ruby/gems/2.2.0/gems/rubytest-cli-0.2.0/man/rubytest.1.ronn
/usr/lib64/ruby/gems/2.2.0/specifications/rubytest-cli-0.2.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/ruby-test
/usr/bin/rubytest
