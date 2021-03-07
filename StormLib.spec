%define soname libstorm
%define sover 9

Name:           StormLib
Version:        9.23
Release:        1
Summary:        Library for work with Blizzard MPQ archive
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://www.zezula.net/mpq.html
Source0:        https://github.com/ladislav-zezula/StormLib/archive/v%{version}/StormLib-%{version}.tar.gz
#Patch0:         clean-system-tomcrypt.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig(libtomcrypt)
BuildRequires:  pkgconfig(libtommath)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)

%description
StomLib library, an open-source project that can work with Blizzard MPQ archives.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description    devel
StomLib library, an open-source project that can work with Blizzard MPQ archives.
This package contains development files for %{name}.

%package     -n %{soname}%{sover}
Summary:        %{name} library
Group:          System/Libraries

%description -n %{soname}%{sover}
StomLib library, an open-source project that can work with Blizzard MPQ archives.
This package contains shared library for %{name}.

%prep
%setup -q
%autopatch -p1

# Remove bundled libraries (we use system provided ones)
rm -v -r src/{zlib,bzip2}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DSTORM_BUILD_TESTS=OFF -DBUILD_DYNAMIC_MODULE=ON -DWITH_LIBTOMCRYPT=ON
%make_build

%install
%make_install -C build
%ifarch x86_64
mv -v %{buildroot}/%{_prefix}/lib %{buildroot}/%{_libdir}
%endif


%files -n %{soname}%{sover}
%defattr(-,root,root)
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%defattr(-,root,root)
%doc README
%license LICENSE
%{_includedir}/Storm*
%{_libdir}/%{soname}.so
