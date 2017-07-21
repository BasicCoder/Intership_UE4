// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/SpinBox.h"

#include "Runtime/UMG/Public/UMG.h"
#include "Runtime/UMG/Public/Components/SpinBox.h"

#include "IntSpinBox.generated.h"

/**
 * 
 */
UCLASS()
class PROJECTTESTSPINBOX_API UIntSpinBox : public USpinBox
{
	GENERATED_BODY()
	
protected:

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Input Data")
		int32 IntegerValue;
	
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Input Data")
		FText DisplayValue;

public:
	UIntSpinBox();

	virtual TSharedRef<SWidget> RebuildWidget() override;

	UFUNCTION(BlueprintCallable, Category = "User Input")
		void MyHandleOnValueChanged(float InValue);

	UFUNCTION(BlueprintCallable, Category = "User Input")
		bool ValiddateIntegerValue(float& InValue);

	UFUNCTION(BlueprintCallable, Category = "User Input")
		int32 GetIntFromFloat(const float& FloatValue);

	UFUNCTION(BlueprintCallable, Category = "User Input")
		void UpdateDisplayValue();

};
