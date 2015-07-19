%define prerelease 74691fb6f83716190870cde1b658538dd4b18eb0
%define import_path code.google.com/p/gosqlite
%define gosrc %{go_dir}/src/pkg/%{import_path}
%define shortcommit %(c=%{prerelease}; echo ${c:0:12})

Summary:	Trivial sqlite3 binding for Go
Name:		golang-sqlite
Version:	0.1.git%{shortcommit}
Release:	5
License:	BSD
Group:		Development/Other
Url:		http://gosqlite.googlecode.com
Source0:	http://gosqlite.googlecode.com/archive/%{prerelease}.zip
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/sqlite) = %{version}-%{release}
Provides:       golang(%{import_path}/sqlite3) = %{version}-%{release}
BuildArch:	noarch
BuildRequires:	golang

%description
Trivial sqlite3 binding for Go

%prep
cd %{_builddir}
unzip %{SOURCE0}

%build
cd %{_builddir}/gosqlite-%{shortcommit}

%install
mkdir -p %{buildroot}%{gosrc}
cp -av %{_builddir}/gosqlite-%{shortcommit}/* %{buildroot}%{gosrc}/

%files
%{gosrc}/*
