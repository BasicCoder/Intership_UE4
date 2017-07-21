# UE4 Limit Input Interger

在项目中需要用户输入一个整数，有两种方案来处理这种情况： 
## Widget Spin Box Limit Input Interger 
**1.** 利用 `spin box` 可以很好的限定用户输入的为数字，但是 UE4 自带的 `spin box` 默认的 Value 为 **float** :  

> 	public:
> 	     /** Value stored in this spin box */
> 	     UPROPERTY(EditAnywhere, Category=Content)
> 	     float Value;

虽然可以很容易通过 `truncate` 或者 `round` 解决限定用户输入为整形，但是默认显示为浮点类型，但是可以通过继承 `spin box` 来生成自己的 `int spin box` 来解决这个问题。  

MyIntegerSpinBox.h 文件：
		
	//MyIntegerSpinBox.h
     
 	#include "Runtime/UMG/Public/UMG.h"
 	#include "Runtime/UMG/Public/Components/SpinBox.h"
     
 	#include "MyIntegerSpinBox.generated.h"
     
 	UCLASS(Blueprintable, BlueprintType)
 	class MYGAME_API UMyIntegerSpinBox : public USpinBox
	{
     GENERATED_BODY()
 
 	protected:
 
	     //within the spin box this is an optional value since we don't need it to restore
	     //non-numeric input; if you choose you can just use the native float Value
	     //and convert it to int when required
	     UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Input Data")
	     int32 IntegerValue;
	 
	     //this is an entirely optional value that your designers can use to
	     //create alternative displays of the current, validated IntegerValue
	     UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Input Data")
	     FText DisplayValue;
 
 	public:
 
	     UMyIntegerSpinBox();
	 
	     //~ Begin UWidget Interface
	     virtual TSharedRef<SWidget> RebuildWidget() override;
	     // End of UWidget
	 
	     UFUNCTION(BlueprintCallable, Category = "User Input")
	     void MyHandleOnValueChanged(float InValue);
	 
	     UFUNCTION(BlueprintCallable, Category = "User Input")
	     bool ValidateIntegerValue(float& InValue);
	 
	     UFUNCTION(BlueprintCallable, Category = "User Input")
	     int32 GetIntFromFloat(const float& FloatValue);
	 
	     UFUNCTION(BlueprintCallable, Category = "User Input")
	     void UpdateDisplayValue();
 
 	};

MyIntegerSpinBox.cpp 文件：
     
 	//MyIntegerSpinBox.cpp
 
 	#include "MyGame.h"
 
 	#include "MyIntegerSpinBox.h"
     
 	UMyIntegerSpinBox::UMyIntegerSpinBox():
		USpinBox(),
		IntegerValue(GetIntFromFloat(Value)),
	    DisplayValue(FText::AsNumber(IntegerValue))
	 	{}
 
 	TSharedRef<SWidget> UMyIntegerSpinBox::RebuildWidget()
 	{
	     MySpinBox = SNew(SSpinBox<float>)
	         .Style(&WidgetStyle)
	         .Font(Font)
	         .ClearKeyboardFocusOnCommit(ClearKeyboardFocusOnCommit)
	         .SelectAllTextOnCommit(SelectAllTextOnCommit)
	         .OnValueChanged(BIND_UOBJECT_DELEGATE(FOnFloatValueChanged, MyHandleOnValueChanged))
	         .OnValueCommitted(BIND_UOBJECT_DELEGATE(FOnFloatValueCommitted, HandleOnValueCommitted))
	         .OnBeginSliderMovement(BIND_UOBJECT_DELEGATE(FSimpleDelegate, HandleOnBeginSliderMovement))
	         .OnEndSliderMovement(BIND_UOBJECT_DELEGATE(FOnFloatValueChanged, HandleOnEndSliderMovement))
	         ;
	     return BuildDesignTimeWidget(MySpinBox.ToSharedRef());
 
 	}
 
 	void UMyIntegerSpinBox::MyHandleOnValueChanged(float InValue) {
	     if (ValidateIntegerValue(InValue)) {
	         HandleOnValueChanged(InValue);
	     }
	}
 
	bool UMyIntegerSpinBox::ValidateIntegerValue(float& InValue) {
	     //checking to make sure the value is different prevents an infinite loop via SetValue
	     if (Value != InValue) {
	         //round up or down, depending on where we're going
	         InValue = Value < InValue ? FMath::CeilToFloat(InValue) : FMath::FloorToFloat(InValue);
	 
	         //then we have to set the value back to the spinner
	         SetValue(InValue);
	 
	         //we can store the integer value if desired
	         IntegerValue = GetIntFromFloat(InValue);
	         //you can use CeilToFlot or Floor if you prefer
	         //IntegerValue = FMath::CeilToFloat(InValue);
	         //IntegerValue = FMath::Floor(InValue);
	 
	         //finally, update the optional FText display value
	         UpdateDisplayValue();
	         return true;
	 
	     }
	     return false;
	 
	}
 
	int32 UMyIntegerSpinBox::GetIntFromFloat(const float& FloatValue) {
	     if (FloatValue >= 0.0f) {
	         return (int)(FloatValue + 0.5f);
	 
	     }
	     return (int)(FloatValue - 0.5f);
	 
	}
	 
	void UMyIntegerSpinBox::UpdateDisplayValue() {
	     DisplayValue = FText::AsNumber(IntegerValue);
	 
	}

## Widget Text Box Limit Input Interger 
**2.** 利用 `Text Box` 用户输入的随意性更大，需要更多限制，经过尝试，Text Box很好的解决了限定用户输入为整数问题。