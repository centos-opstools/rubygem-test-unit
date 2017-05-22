%global	gem_name	test-unit

# svn repository
# http://test-unit.rubyforge.org/svn/trunk/

Summary:	Improved version of Test::Unit bundled in Ruby 1.8.x
Name:		rubygem-%{gem_name}
Version:	3.1.9
Release:	2%{?dist}
Group:		Development/Languages
# lib/test/unit/diff.rb is under GPLv2 or Ruby or Python
# lib/test-unit.rb is under LGPLv2+ or Ruby
# Other file: GPLv2 or Ruby
License:	Ruby and PSFL
URL:		http://test-unit.github.io/

Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems
BuildRequires:	rubygems-devel
# For %%check
#BuildRequires:	rubygem(rake)
#BuildRequires:	rubygem(hoe)
Requires:	ruby(release)
Requires:	rubygems
Requires: rubygem(power_assert)

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Test::Unit 3.x - Improved version of Test::Unit bundled in
Ruby 1.8.x.
Ruby 1.9.x bundles minitest not Test::Unit. Test::Unit
bundled in Ruby 1.8.x had not been improved but unbundled
Test::Unit (Test::Unit 3.x) will be improved actively.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
#rake test --trace
ruby -Ilib ./test/run-test.rb
popd

%files
%defattr(-,root,root,-)
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%{gem_instdir}/GPL
%{gem_instdir}/LGPL
%{gem_instdir}/PSFL
%{gem_libdir}
%{gem_instdir}/sample
%exclude %{gem_cache}
%{gem_spec}

%files	doc
%defattr(-,root,root,-)
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/test

%changelog
* Thu Sep 22 2016 Rich Megginson <rmeggins@redhat.com> - 3.1.9-2
- bump rev to rebuild for buildroot

* Fri Sep 16 2016 Rich Megginson <rmeggins@redhat.com> - 3.1.9-1
- version 3.1.9

* Thu Jul 18 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.5-1
- 2.5.5

* Thu Feb 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.4-3
- Patch for CSV support (patch by upstream)

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.4-2
- Rebuild for ruby 2.0.0

* Sun Feb  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.4-1
- 2.5.4

* Thu Jan  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.3-1
- 2.5.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-3
- Fix conditionals for F17 to work for RHEL 7 as well.

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.4.5-2
- 2.4.5

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.4.4-1
- 2.4.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.4.3-1
- 2.4.3

* Sun Nov 27 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.4.2-1
- 2.4.2

* Wed Nov 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.4.1-1
- 2.4.1

* Mon Sep 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.4.0-1
- 2.4.0

* Thu Aug 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.3.2-1
- 2.3.2

* Sun Aug 14 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.3.1-1
- 2.3.1

* Sun Apr 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.3.0-1
- 2.3.0

* Fri Feb 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Mon Feb 14 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.2-2
- F-15 mass rebuild

* Fri Nov 26 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.2-1
- 2.1.2

* Sun Sep 19 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.1-2
- Fix up license tag

* Sat Sep 18 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.1.1-1
- Initial package
