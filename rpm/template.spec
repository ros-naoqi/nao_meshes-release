Name:           ros-indigo-nao-meshes
Version:        0.1.9
Release:        0%{?dist}
Summary:        ROS nao_meshes package

Group:          Development/Libraries
License:        Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License
URL:            http://github.com/vrabaud/nao_meshes/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  java-1.7.0-openjdk
BuildRequires:  java-1.8.0-openjdk
BuildRequires:  ros-indigo-catkin

%description
meshes for the Aldebaran Robotics NAO

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Jan 24 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.9-0
- Autogenerated by Bloom

* Thu Nov 27 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.8-0
- Autogenerated by Bloom

* Fri Oct 03 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.7-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.6-0
- Autogenerated by Bloom

* Thu Sep 04 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.5-0
- Autogenerated by Bloom

* Thu Sep 04 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.4-0
- Autogenerated by Bloom

* Wed Sep 03 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

* Fri Aug 29 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

* Wed Aug 27 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.1-1
- Autogenerated by Bloom

* Wed Aug 27 2014 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Vincent Rabaud <vrabaud@aldebaran-robotics.com> - 0.1.0-1
- Autogenerated by Bloom

* Tue Aug 26 2014 Vincent Rabaud <vrabaud@aldebaran-robotics.com> - 0.1.0-0
- Autogenerated by Bloom

