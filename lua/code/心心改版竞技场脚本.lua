if FX2 == nil then
  mm = gg.prompt({[1]="请输入密码"}, {[1]="0"}, {[1]="txet"})
  if mm[1] == "2844188533" then
    gg.toast("密码正确")
  else
    print(mm[1],"密码错误")
    os.exit()
  end
end

function A()
CD = gg.choice({
         "⁣①无敌一(联网开)\n Ca+类内存",--1
         "⁣①恢复",--2
         "②无敌二\n Other类内存",--3
         "②恢复",--4
         "③退出",--5
    },"nil","我若喜欢什么.心里就在容不下别的.永远都会记着")
if CD == 1 then a() end
if CD == 2 then b() end
if CD == 3 then c() end
if CD == 4 then d() end
if CD == 5 then e() end
JC = 0 end


function a()
gg.toast(os.date("%Y年-%m月-%d日 %H时:%M分:%S秒"))
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC)
gg.searchNumber("2,147,483,648D;0F;-127D;1;-125D;-120D::25", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
gg.searchNumber("-127", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
gg.getResults(50)
gg.editAll("9", gg.TYPE_DWORD)
gg.clearResults()
gg.toast("成功")
end

function b()
gg.toast(os.date("%Y年-%m月-%d日 %H时:%M分:%S秒"))
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC)
gg.searchNumber("2,147,483,648D;0F;9D;1;-125D;-120D::25", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
gg.searchNumber("9", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
gg.getResults(50)
gg.editAll("-127", gg.TYPE_DWORD)
gg.toast("成功")
end

function c()
gg.toast(os.date("%Y年-%m月-%d日 %H时:%M分:%S秒"))
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC)
gg.searchNumber("1D;-127D;2D;-127D;3D;-127D;4D;-127D::29", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
gg.searchNumber("4", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
gg.getResults(50)
gg.editAll("9", gg.TYPE_DWORD)
gg.clearResults()
gg.toast("成功")
end

function d()
gg.toast(os.date("%Y年-%m月-%d日 %H时:%M分:%S秒"))
gg.clearResults()
gg.setRanges(gg.REGION_C_ALLOC)
gg.searchNumber("1D;-127D;2D;-127D;3D;-127D;9D;-127D::29", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
gg.searchNumber("9", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
gg.getResults(50)
gg.editAll("4", gg.TYPE_DWORD)
gg.toast("成功")
end

function e()
gg.skipRestoreState()
gg.setVisible(true)
os.exit()
end

repeat
if gg.isVisible(true) then
JC = 1
gg.setVisible(false)
end
if JC == 1 then
A()
end
until false